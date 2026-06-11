import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

st.title("InterviewGPT")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

question = st.text_input("Ask a question")

if st.button("Submit"):

    docs = db.similarity_search(
        question,
        k=3
    )

    st.write("Retrieved Chunks:")

    for doc in docs:
        st.write(doc.page_content[:300])