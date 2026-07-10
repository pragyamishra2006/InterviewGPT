# 🤖 InterviewGPT – AI-Powered Placement Preparation Assistant

InterviewGPT is an AI-powered Placement Preparation Assistant built using **Retrieval-Augmented Generation (RAG)**. It enables users to upload placement preparation PDFs, perform semantic search over their study materials, and receive context-aware answers using a locally hosted Large Language Model (LLM).

The application combines **document processing, vector embeddings, semantic retrieval, and local LLM inference** to provide accurate and relevant responses without relying on cloud-based AI services.

---

## 🚀 Features

- 📄 Upload one or multiple PDF documents
- 🔍 Semantic search using vector embeddings
- 🤖 Context-aware AI question answering
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 💾 Persistent vector storage with ChromaDB
- 🦙 Local LLM inference using Ollama
- 🌐 Interactive Streamlit web interface
- ⚡ Fast document retrieval and response generation
- 🔒 Fully local processing for enhanced privacy

---

## 🏗️ System Architecture

```
                 PDF Upload
                      │
                      ▼
             Text Extraction
                      │
                      ▼
             Document Chunking
                      │
                      ▼
         HuggingFace Embeddings
                      │
                      ▼
          ChromaDB Vector Store
                      │
                      ▼
           Semantic Retrieval
                      │
                      ▼
              Ollama LLM
                      │
                      ▼
        Context-Aware AI Response
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| LLM Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | Hugging Face Sentence Transformers |
| Local LLM | Ollama |
| Document Processing | PyPDF |

---

## 📂 Project Structure

```text
InterviewGPT/
│
├── app.py                     # Streamlit application
├── chroma_db/                 # Vector database
├── uploads/                   # Uploaded PDF files
│
├── src/
│   ├── loader.py              # PDF loading
│   ├── chunker.py             # Document chunking
│   ├── vector_store.py        # ChromaDB integration
│   ├── retriever.py           # Semantic retrieval
│   ├── ingest.py              # Data ingestion pipeline
│   └── chat.py                # LLM interaction
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pragyamishra2006/InterviewGPT.git
cd InterviewGPT
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download Ollama from:

https://ollama.com

Pull a language model:

```bash
ollama pull qwen2.5:1.5b
```

Verify installation:

```bash
ollama list
```

---

## 📚 Add Your Documents

Upload PDFs directly from the web interface or place them inside the `uploads/` directory.

Example documents:

- Data Structures & Algorithms
- Operating Systems
- DBMS
- Computer Networks
- Interview Experiences
- Aptitude Notes

---

## 🔄 Build the Knowledge Base

Run the ingestion pipeline:

```bash
python src/ingest.py
```

This pipeline:

- Loads PDF documents
- Extracts text
- Splits text into semantic chunks
- Generates vector embeddings
- Stores embeddings in ChromaDB

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 💬 Example Questions

- Explain Binary Search.
- What are ACID Properties?
- Difference between TCP and UDP?
- Explain Deadlock.
- What is Process Synchronization?
- What are Virtual Functions in C++?

---

## 📸 Screenshots

### Home Page

> *(Add screenshot here)*

### Upload Documents

> *(Add screenshot here)*

### Chat Interface

> *(Add screenshot here)*

---

## 📌 Future Enhancements

- 🎤 AI Mock Interview Mode
- 📄 Resume Analyzer
- 💼 Company-wise Interview Questions
- 📈 Placement Progress Tracker
- 💬 Chat History
- 🌍 Multi-language Support
- 📊 Analytics Dashboard
- 🐳 Docker Deployment

---

## 🎯 Key Learnings

This project helped me gain hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- Document Embeddings
- LangChain Pipelines
- Local AI Deployment
- Streamlit Application Development

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pragya Mishra**

- GitHub: https://github.com/pragyamishra2006

---

⭐ **If you found this project useful, please consider giving it a star!**
