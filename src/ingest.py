

from loader import load_documents
from chunker import split_docs
from vector_store import create_vector_store

print("Loading PDFs...")

docs = load_documents()

print("Total Pages:", len(docs))

chunks = split_docs(docs)

print("Total Chunks:", len(chunks))

db = create_vector_store(chunks)

print("Vector DB created successfully!")