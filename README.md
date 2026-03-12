# Iterative Deep Research Engine

An AI-powered research system that performs web search, retrieves relevant sources, and generates grounded answers using a Retrieval-Augmented Generation (RAG) pipeline.

The system automatically gathers information from the web, processes documents, stores embeddings in a vector database, and generates answers with citations.

This project demonstrates how modern AI systems like Perplexity-style research assistants are built.

---

# Features

* Web search integration for real-time information
* Automatic webpage fetching and processing
* Document chunking and embedding generation
* Vector search using Qdrant
* Hybrid retrieval for better context selection
* Reranking for higher quality sources
* Retrieval-Augmented Generation (RAG)
* Source-backed answers

---

# System Architecture

User Query
↓
Web Search
↓
Page Fetching
↓
Document Chunking
↓
Embeddings (Sentence Transformers)
↓
Vector Database (Qdrant)
↓
Hybrid Retrieval
↓
Reranking
↓
LLM Generation
↓
Final Answer + Sources

---

# Tech Stack

Backend

* Python
* FastAPI

AI / ML

* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

Database

* Qdrant Vector Database

LLM APIs

* External LLM providers for generation

Infrastructure

* Python virtual environments
* REST API architecture

---

# Installation

Clone the repository:

git clone https://github.com/Dev048/iterative-deep-research-engine.git

cd iterative-deep-research-engine

Install dependencies:

pip install -r requirements.txt

Create environment file:

cp .env.example .env

Add your API keys to the `.env` file.

Run the API server:

uvicorn backend.app.main:app --reload

---

# Usage

Send a query to the research endpoint.

Example request:

POST /research

{
"query": "latest breakthroughs in robotics"
}

The system will:

1. Search the web
2. Retrieve relevant documents
3. Rank sources
4. Generate an answer using RAG

---

# Example Output

Query

"What are recent breakthroughs in robotics?"

Answer

Recent breakthroughs in robotics include improvements in AI-driven control systems, humanoid robot development, and advances in robotic manipulation.

Sources

* https://example-source-1.com
* https://example-source-2.com

---

# Project Structure

backend/
app/
api/
retrieval/
embeddings/
rag/
services/
main.py

frontend/

tests/

docs/

examples/

assets/

README.md
requirements.txt
.env.example

---

# Future Improvements

* Multi-agent research workflows using LangGraph
* Streaming responses
* Improved ranking models
* Long-term memory for research sessions
* UI for interactive research

---

# License

This project is released under the MIT License.
