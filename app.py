import streamlit as st
import ollama
import os
import subprocess

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="InterviewGPT",
    page_icon="🤖",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #1f77b4;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

.answer-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f5f7fa;
    border-left: 6px solid #1f77b4;
    margin-top: 10px;
}

.metric-box {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 InterviewGPT")

    st.markdown("---")

    st.write("### Features")

    st.write("📚 Learn from Notes")
    st.write("🎯 Placement Preparation")
    st.write("💻 DSA / OS / DBMS / CN")
    st.write("🧠 AI Question Answering")
    st.write("🤖 Mock Interview (Coming Soon)")

    st.markdown("---")

    st.success("Model: Qwen 2.5")
    st.info("Vector DB: ChromaDB")
    st.markdown("---")

    os.makedirs("uploads", exist_ok=True)

    st.subheader("📂 Upload Notes")

    uploaded_file = st.file_uploader(
    "Upload PDF Notes",
    type=["pdf"],
    key="notes_uploader"
    )

    if uploaded_file:

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(
            f"✅ {uploaded_file.name} uploaded"
        )

        with st.spinner(
            "🔄 Updating Knowledge Base..."
        ):

            subprocess.run(
            ["python", "src/ingest.py"]
            )

        st.success(
            "✅ Knowledge Base Updated"
        )
    
    
# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">🤖 InterviewGPT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Placement Preparation Assistant using RAG + Ollama</div>',
    unsafe_allow_html=True
)

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("LLM", "Qwen 2.5")

with col2:
    st.metric("Vector DB", "Chroma")

with col3:
    st.metric("Status", "Online")

st.markdown("---")

# ---------------- LOAD VECTOR DB ----------------

@st.cache_resource
def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db

db = load_db()

# ---------------- QUESTION INPUT ----------------

question = st.text_area(
    "💬 Ask a Question",
    placeholder="Example: What is Cyber Security?",
    height=120
)

# ---------------- BUTTON ----------------

if st.button("🚀 Get Answer", use_container_width=True):

    if not question.strip():

        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("🔍 Searching your notes..."):

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
            st.session_state.history.append(
                {
                    "question": question,
                    "answer": answer
                }
            )
            st.markdown("## 🎯 Answer")
            st.markdown(answer)
            

            st.success("Answer generated successfully!")
            st.markdown("### 📚 Sources")

            sources = set()

            for doc in docs:

                source = doc.metadata.get(
                "source",
                "Unknown File"
                )

                sources.add(source)

            for source in sources:

                st.write("📄", source)
        except Exception as e:

            st.error(f"Error: {str(e)}")

    # ---------------- CONTEXT VIEWER ----------------

    with st.expander("📄 Retrieved Context"):

        for i, doc in enumerate(docs, start=1):

            st.markdown(f"### Chunk {i}")

            st.write(doc.page_content)
            
    if st.session_state.history:
    
        st.markdown("---")

        st.markdown("## 🕒 Chat History")

        for item in reversed(
            st.session_state.history
        ):

            st.write(
                f"**Q:** {item['question']}"
            )

            st.write(
                f"**A:** {item['answer']}"
            )

            st.markdown("---")       
            

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit, LangChain, ChromaDB, Ollama and Qwen 2.5"
)