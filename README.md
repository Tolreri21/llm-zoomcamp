# llm-zoomcamp
My self-paced work through LLM Zoomcamp (DataTalks.Club): RAG pipelines, vector search, agents, evaluation and monitoring.

Course: https://github.com/DataTalksClub/llm-zoomcamp

## Structure

```
01-agentic-rag/     # module 1: RAG with keyword search, sqlitesearch, function calling
02-vector-search/   # module 2: embeddings, sqlitesearch vectors, pgvector
src/llm_zoomcamp/   # shared code (ingest, RAGBase) — import as `llm_zoomcamp.*`
scripts/            # standalone helper scripts
data/               # local SQLite indexes (git-ignored)
```

## Setup

```bash
uv sync
cp .env.example .env   # add your API key
```
