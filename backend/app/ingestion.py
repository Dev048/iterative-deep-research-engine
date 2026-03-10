from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from uuid import uuid4

from app.embeddings import embed_text
from app.chunking import chunk_text

client = QdrantClient(host="localhost", port=6333)

COLLECTION = "research_docs"


def ingest_document(text: str):

    chunks = chunk_text(text)

    points = []

    for chunk in chunks:
        vector = embed_text(chunk)

        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=COLLECTION,
        points=points
    )

    print(f"Inserted {len(points)} chunks")