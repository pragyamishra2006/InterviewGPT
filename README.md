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

<img width="920" height="408" alt="{472E9B0A-72FF-4560-A16C-3C9C28D41042}" src="https://github.com/user-attachments/assets/0a92cfb3-c475-4a47-a06c-4b4427f8b63a" />


### Upload Documents

<img width="638" height="392" alt="{4A14C52D-2D5B-41F7-83A8-FF80D5E14D92}" src="https://github.com/user-attachments/assets/5aafdd5a-74c0-47dd-b49f-d8e24778da4a" />

### Chat Interface

<img width="670" height="382" alt="{195C3CE6-9449-4675-AEDA-E156419AD285}" src="https://github.com/user-attachments/assets/68ca65b2-6703-40d1-8980-0c55d7c5df96" />

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
