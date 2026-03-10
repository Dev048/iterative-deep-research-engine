from qdrant_client import QdrantClient
from app.embeddings import embed_text

client = QdrantClient(host="localhost", port=6333)

COLLECTION = "research_docs"


def search(query: str, limit: int = 3):

    query_vector = embed_text(query)

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=limit
    )

    return [point.payload["text"] for point in results.points]