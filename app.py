import streamlit as st
import ollama

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Page Configuration
st.set_page_config(
    page_title="InterviewGPT",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 InterviewGPT")
st.write("Ask questions from your uploaded notes.")

# Load Vector Database
@st.cache_resource
def load_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db

db = load_db()

# User Input
question = st.text_input(
    "Ask a Question"
)

# Ask Button
if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching your notes..."):

        # Retrieve relevant chunks
        docs = db.similarity_search(
            question,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are InterviewGPT.

Answer the question only using the provided context.

If the answer is not present in the context,
say: "I could not find the answer in the uploaded notes."

Context:
{context}

Question:
{question}
"""

        try:

            response = ollama.chat(
                model="qwen2.5:1.5b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response["message"]["content"]

            st.subheader("Answer")
            st.write(answer)

        except Exception as e:

            st.error(
                f"Ollama Error: {str(e)}"
            )

    with st.expander("Retrieved Context"):

        for i, doc in enumerate(docs, 1):

            st.markdown(f"### Chunk {i}")

            st.write(
                doc.page_content[:1000]
            )