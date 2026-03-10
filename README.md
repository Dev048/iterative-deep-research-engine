# Iterative Deep Research Engine

An AI research assistant that performs iterative web search, document ingestion, and retrieval augmented generation to produce comprehensive answers.

## Architecture

User Query
   ↓
Web Search
   ↓
Page Fetching
   ↓
Document Chunking
   ↓
Embeddings
   ↓
Vector Store (Qdrant)
   ↓
Hybrid Retrieval
   ↓
Reranking
   ↓
RAG Generation
   ↓
Final Answer

## Features

- Web search ingestion
- Document chunking
- Embedding generation
- Vector database storage
- Hybrid retrieval
- Reranking
- Retrieval Augmented Generation

## Tech Stack

Python  
FastAPI  
Qdrant  
Sentence Transformers  
LLMs

## Project Structure

backend/app
- chunking.py
- embeddings.py
- ingestion.py
- retrieval.py
- reranker.py
- vector_store.py
- rag.py
- web_search.py

frontend
- index.html

tests
- unit tests for retrieval, embeddings, chunking

## Running the Project

Install dependencies

pip install -r requirements.txt

Create environment file

.env

Then run:

python backend/app/main.py

## Architecture Overview

This system implements an iterative research pipeline using
retrieval augmented generation (RAG).

Pipeline stages:

1. Web search
2. Page fetching
3. Document chunking
4. Embedding generation
5. Vector storage (Qdrant)
6. Hybrid retrieval
7. Reranking
8. LLM answer generation
