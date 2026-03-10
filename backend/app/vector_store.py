from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


client = QdrantClient(host="localhost", port=6333)

COLLECTION = "web_chunks"


def ensure_collection():
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION not in names:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            ),
        )


def clear_collection():
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        ),
    )


def insert_chunks(chunks, embed_fn):

    points = []

    for chunk in chunks:
        vector = embed_fn(chunk)

        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={"text": chunk},
            )
        )

    if points:
        client.upsert(
            collection_name=COLLECTION,
            points=points
        )


def search_chunks(query_vector, limit=8):

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=limit,
    )

    return [p.payload["text"] for p in results.points]