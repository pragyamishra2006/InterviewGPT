# 🤖 InterviewGPT

InterviewGPT is an AI-powered Placement Preparation Assistant built using Retrieval-Augmented Generation (RAG). It allows users to upload study materials and ask questions directly from their notes using a local Large Language Model.

## 🚀 Features

* 📄 Upload PDF Notes
* 🔍 Semantic Search using Vector Embeddings
* 🤖 AI-Powered Question Answering
* 📚 Context-Aware Responses
* 💾 ChromaDB Vector Database
* 🧠 Local LLM Inference with Ollama
* 🌐 Interactive Streamlit Web Interface

## 🛠 Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Ollama
* Hugging Face Embeddings
* Sentence Transformers

## 📂 Project Structure

```bash
InterviewGPT/
│
├── app.py
├── chroma_db/
├── uploads/
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── ingest.py
│   └── chat.py
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pragyamishra2006/InterviewGPT.git
cd InterviewGPT
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🦙 Setup Ollama

Install Ollama and pull a model:

```bash
ollama pull qwen2.5:1.5b
```

Verify installation:

```bash
ollama list
```

## 📚 Add Notes

Place your PDF notes inside the uploads folder or upload them through the web interface.

Examples:

* DSA Notes
* Operating Systems Notes
* DBMS Notes
* Computer Networks Notes
* Interview Experiences

## 🔄 Create Vector Database

```bash
python src/ingest.py
```

This will:

* Load PDFs
* Split documents into chunks
* Generate embeddings
* Store vectors in ChromaDB

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

## 💬 Example Questions

* What is Cyber Security?
* Explain Deadlock in Operating Systems.
* What are ACID Properties in DBMS?
* Explain TCP vs UDP.
* What is Binary Search?

## 📸 Demo

Upload your notes and ask questions in natural language. InterviewGPT retrieves relevant context from your documents and generates answers using a local LLM.

## 🎯 Future Improvements

* Mock Interview Mode
* Interview Question Generator
* Multi-PDF Knowledge Base
* Chat History
* Resume Analyzer
* Placement Roadmap Generator

## 🌟 Learning Outcomes

This project helped me gain practical experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* LangChain
* Local LLM Deployment
* Streamlit Application Development

## 👨‍💻 Author

Pragya Mishra

GitHub:
https://github.com/pragyamishra2006

---

⭐ If you found this project interesting, consider giving it a star.
