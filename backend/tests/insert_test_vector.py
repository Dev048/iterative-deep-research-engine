from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(host="localhost", port=6333)

vector = [0.1] * 384

client.upsert(
    collection_name="research_docs",
    points=[
        PointStruct(
            id=1,
            vector=vector,
            payload={"text": "test document"}
        )
    ]
)

print("Vector inserted")