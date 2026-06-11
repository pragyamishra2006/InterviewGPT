from loader import docs
from chunker import split_docs
from vector_store import create_vector_store

chunks = split_docs(docs)

print("Chunks:", len(chunks))

db = create_vector_store(chunks)

print("Vector DB created successfully")