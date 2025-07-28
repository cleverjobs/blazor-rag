#!/usr/bin/env python3
"""End-to-end ingestion script

Usage inside the *ingest-worker* container (docker-compose):

    docker compose run --rm ingest-worker

The script reads **pre-processed manifests** produced by the scraping/normalising
stage, chunks their Markdown, embeds each chunk with a HuggingFace model, and
upserts everything into a local Qdrant collection.

Environment vars (all optional):
    MANIFEST_DIR       Where the *.jsonl manifests live          (default: /data/manifests)
    COLLECTION_NAME    Qdrant collection name                    (default: telerik_blazor_docs)
    QDRANT_URL         Host or host:port of Qdrant               (default: qdrant:6333)
    EMBED_MODEL        HF model id for embeddings                (default: BAAI/bge-large-en-v1.5)
    WINDOW_SIZE        Chunk window (tokens)                     (default: 400)
    WINDOW_OVERLAP     Chunk overlap (tokens)                    (default: 50)

Prereqs: packages in backend/requirements.txt (FastAPI image already has them).
"""

from __future__ import annotations

import json
import os
import re
import sys
from itertools import islice
from pathlib import Path
from typing import Dict, List, Sequence

import tqdm
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient, models

###############################################################################
# Helpers
###############################################################################

BATCH = 256  # points per upsert


def batched(iterable: Sequence, n: int):
    """Yield successive n-sized chunks from *iterable*."""
    for i in range(0, len(iterable), n):
        yield iterable[i : i + n]


###############################################################################
# Config
###############################################################################

MANIFEST_DIR = Path(os.getenv("MANIFEST_DIR", "/data/manifests"))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "telerik_blazor_docs")
QDRANT_URL = os.getenv("QDRANT_URL", "qdrant:6333")
EMBED_MODEL_ID = os.getenv("EMBED_MODEL", "BAAI/bge-large-en-v1.5")
WINDOW_SIZE = int(os.getenv("WINDOW_SIZE", 400))
WINDOW_OVERLAP = int(os.getenv("WINDOW_OVERLAP", 50))

HOST, *maybe_port = QDRANT_URL.split(":")
PORT = int(maybe_port[0]) if maybe_port else 6333

###############################################################################
# Load manifests
###############################################################################

print("[ingest] Reading manifests from", MANIFEST_DIR)
records: List[Dict] = []
for name in ("docs.jsonl", "forum.jsonl"):
    p = MANIFEST_DIR / name
    if not p.exists():
        print(f"[warn] Manifest missing: {p}")
        continue
    records.extend(json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line)

if not records:
    print("[error] No manifest entries found – aborting.")
    sys.exit(1)

print(f"[ingest] Loaded {len(records):,} manifest entries")

###############################################################################
# Initialise models
###############################################################################

print("[ingest] Loading embed model", EMBED_MODEL_ID)
embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_ID)

chunker = SentenceWindowNodeParser(
    window_size=WINDOW_SIZE,
    window_overlap=WINDOW_OVERLAP,
    break_on_newline=True,
)

###############################################################################
# Prepare Qdrant collection
###############################################################################

client = QdrantClient(host=HOST, port=PORT)
vector_dim = embed_model.get_text_embedding("test").__len__()

# Always recreate collection to ensure correct vector dimensions
print(f"[ingest] Creating collection '{COLLECTION_NAME}' (dim={vector_dim})")
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(size=vector_dim, distance=models.Distance.COSINE),
)

###############################################################################
# Chunk → Embed → Upsert
###############################################################################

def process_record(rec: Dict) -> List[Dict]:
    """Return list of node dicts ready for Qdrant."""
    # Use 'file_path' key from manifest, fallback to 'path'
    file_path = rec.get("file_path") or rec.get("path")
    if not file_path:
        raise ValueError(f"No file_path or path found in record: {rec}")
    
    path = Path(file_path)
    # If path is relative, resolve from container root
    if not path.is_absolute():
        path = Path("/") / path
    
    text = path.read_text(encoding="utf-8")

    doc_obj = Document(text=text, metadata=rec)
    nodes = chunker.get_nodes_from_documents([doc_obj])

    for n in nodes:
        n.embedding = embed_model.get_text_embedding(n.text)

    return [
        {
            "id": n.node_id,
            "vector": n.embedding,
            "payload": {
                "text": n.text,
                **rec,  # merge original metadata so we keep title, url, etc.
            },
        }
        for n in nodes
    ]

all_points: List[Dict] = []
print("[ingest] Chunking + embedding …")
for rec in tqdm.tqdm(records):
    try:
        all_points.extend(process_record(rec))
    except Exception as e:
        file_path = rec.get("file_path") or rec.get("path", "unknown")
        print(f"[warn] Failed: {file_path} – {e}")

print(f"[ingest] Total chunks to upsert: {len(all_points):,}")

for batch in tqdm.tqdm(list(batched(all_points, BATCH)), desc="upsert"):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=models.Batch(
            ids=[p["id"] for p in batch],
            vectors=[p["vector"] for p in batch],
            payloads=[p["payload"] for p in batch],
        ),
    )

print("[ingest] Done – Qdrant collection populated.")
