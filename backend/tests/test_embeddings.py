from app.embeddings import embed_text

vector = embed_text("Artificial intelligence is transforming healthcare")

print(len(vector))
print(vector[:5])