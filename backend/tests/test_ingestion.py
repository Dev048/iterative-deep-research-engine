from app.ingestion import ingest_document

text = """
Artificial intelligence is transforming healthcare.
Machine learning models assist doctors in diagnosis.
Large language models help analyze medical records.
AI is also used in drug discovery and treatment planning.
"""

ingest_document(text)