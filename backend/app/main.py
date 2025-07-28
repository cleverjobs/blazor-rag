import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient
import requests
import json

app = FastAPI(title="RAG API")

# Allow everything for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
QDRANT_URL = os.getenv("QDRANT_URL", "qdrant:6333")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "telerik_blazor_docs")
EMBED_MODEL_ID = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# Initialize clients
HOST, *maybe_port = QDRANT_URL.split(":")
PORT = int(maybe_port[0]) if maybe_port else 6333
qdrant_client = QdrantClient(host=HOST, port=PORT)
embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_ID)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

class SearchResult(BaseModel):
    text: str
    metadata: dict
    score: float

def search_qdrant(query: str, limit: int = 5) -> List[SearchResult]:
    """Search for relevant chunks in Qdrant."""
    # Get query embedding
    query_embedding = embed_model.get_text_embedding(query)
    
    # Search in Qdrant
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=limit,
        with_payload=True
    )
    
    results = []
    for hit in search_result:
        results.append(SearchResult(
            text=hit.payload.get("text", ""),
            metadata={k: v for k, v in hit.payload.items() if k != "text"},
            score=hit.score
        ))
    
    return results

def generate_response(query: str, context_chunks: List[SearchResult]) -> str:
    """Generate response using Ollama."""
    # Prepare context from search results
    context = "\n\n".join([f"Context {i+1}:\n{chunk.text}" for i, chunk in enumerate(context_chunks)])
    
    # Create prompt
    prompt = f"""Based on the following context about Telerik Blazor components, please answer the user's question. 
If the answer is not found in the context, say so clearly.

Context:
{context}

Question: {query}

Answer:"""

    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": "llama3.2:1b",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("message", {}).get("content", "Sorry, I couldn't generate a response.")
    except Exception as e:
        return f"Error generating response: {str(e)}"

@app.get("/")
def read_root():
    return {"status": "up", "collection": COLLECTION_NAME, "embed_model": EMBED_MODEL_ID}

@app.get("/search")
async def search(q: str, limit: int = 5):
    """Search endpoint for testing retrieval."""
    try:
        results = search_qdrant(q, limit)
        return {"query": q, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """RAG endpoint that searches for relevant context and generates an answer."""
    try:
        # Search for relevant context
        search_results = search_qdrant(req.query, limit=3)
        
        if not search_results:
            return ChatResponse(answer="I couldn't find any relevant information to answer your question.")
        
        # Generate response using Ollama
        answer = generate_response(req.query, search_results)
        
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
