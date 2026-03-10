from concurrent.futures import ThreadPoolExecutor

from app.web_search import search_web
from app.page_fetcher import fetch_page_text
from app.chunking import chunk_text
from app.embeddings import embed_text
from app.llm import generate_answer
from app.vector_store import (
    ensure_collection,
    clear_collection,
    insert_chunks,
    search_chunks,
)
from app.reranker import rerank


def ask(query: str):

    ensure_collection()
    clear_collection()

    search_results = search_web(query)

    urls = [r["url"] for r in search_results]

    documents = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_page_text, urls)

    for text in results:
        if text:
            documents.append(text)

    chunks = []

    for doc in documents:
        chunks.extend(chunk_text(doc))

    if not chunks:
        return {
            "answer": "I could not retrieve useful content from the web.",
            "sources": urls,
        }

    insert_chunks(chunks, embed_text)

    query_vector = embed_text(query)

    retrieved_chunks = search_chunks(query_vector, limit=15)

    best_chunks = rerank(query, retrieved_chunks, top_k=6)

    answer = generate_answer(query, best_chunks)

    return {
        "answer": answer,
        "sources": urls,
    }