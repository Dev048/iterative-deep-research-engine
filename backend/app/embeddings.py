from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")

def embed_text(text: str):
    vector = model.encode(text, normalize_embeddings=True)
    return vector.tolist()