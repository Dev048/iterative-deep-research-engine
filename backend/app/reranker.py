from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, passages, top_k=5):

    pairs = [[query, p] for p in passages]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(passages, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [p for p, _ in ranked[:top_k]]