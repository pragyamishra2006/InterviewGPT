from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )

    return db