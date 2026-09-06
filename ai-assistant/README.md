# AI Assistant — RAG Prototype

> Chunk → hash embed → retrieve → generate stub.

![LLM](https://img.shields.io/badge/LLM-RAG-purple)

## Problem
Retrieve relevant docs for a query.

## Approach
`docs = ["YasirLab builds...", "RAG retrieves...", "LLM generates..."]` → `hash(md5)%100` embed → `sorted by |embed(q)-embed(d)|`.

## Quick start
```bash
python src/rag.py
# ['YasirLab builds ML systems', ...]
```

## YasirLab
AI track — next add vector DB + LLM.
