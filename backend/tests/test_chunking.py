from app.chunking import chunk_text

text = """
Artificial intelligence is transforming healthcare.
Machine learning models assist doctors in diagnosis.
Large language models are being used in research.
AI systems are also improving drug discovery.
"""

chunks = chunk_text(text)

print(len(chunks))
print(chunks)