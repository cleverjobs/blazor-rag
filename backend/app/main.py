from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="RAG API")

# Allow everything for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"status": "up"}

@app.post("/v1/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Stub endpoint – returns an echo until you wire up LlamaIndex."""
    fake_answer = f"Echo: {req.query}"
    return {"answer": fake_answer}
