
# RAG-based Explainability for Kiln Root-Cause Analysis

Demonstrates a **Retrieval-Augmented Generation (RAG)** scaffold to answer "why" questions about kiln anomalies using domain documents (e.g., MES manuals, SOPs). For safety, this demo uses **placeholder docs** and a lightweight retrieval implementation to avoid extra dependencies.

> Real deployments should use LangChain/LangGraph + vector DB (FAISS/Pinecone/pgvector). Here we provide a minimal Python-only retriever and prompt template so it runs anywhere.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/app.py --question "Why did CO spike during the last firing cycle?"
```

## How it works
- Loads text files from `docs/` (replace with your MES manuals/SOPs).
- Builds a simple TF-IDF-like index (sklearn) and retrieves top-k passages.
- Formats a prompt for an LLM (placeholder: rule-based summarizer provided). Swap with Azure OpenAI/OpenAI in `llm.py`.

## Security & Compliance
- No proprietary docs included. Add redaction in `redaction.py` before indexing.

## Extending to LangChain
- Replace `retriever.py` with LC pipeline and add embeddings via `requirements.txt`.
