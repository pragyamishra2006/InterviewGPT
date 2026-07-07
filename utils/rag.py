"""Reusable RAG helpers that preserve the existing retrieval pipeline."""

from __future__ import annotations

import os
import subprocess
import sys
from typing import Any

import ollama
import streamlit as st
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


@st.cache_resource
def load_db() -> Chroma:
    """Load the persistent Chroma vector store."""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings,
    )


def build_context(docs: list[Any]) -> str:
    """Join retrieved chunks into prompt context."""
    return "\n\n".join(doc.page_content for doc in docs)


def build_prompt(question: str, context: str) -> str:
    """Construct the answer-generation prompt."""
    return f"""
You are InterviewGPT, an expert interview preparation assistant.
Answer the question using only the provided context.
If the answer is not present in the context, say:
"I could not find the answer in the uploaded notes."

Context:
{context}

Question:
{question}
"""


def generate_answer(
    question: str,
    docs: list[Any],
    model: str,
    temperature: float,
) -> str:
    """Generate an answer from retrieved context using Ollama."""
    context = build_context(docs)
    prompt = build_prompt(question, context)
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": temperature},
    )
    return response["message"]["content"]


def retrieve_documents(question: str, top_k: int = 4) -> list[Any]:
    """Return semantically relevant chunks for a user question."""
    db = load_db()
    return db.similarity_search(question, k=top_k)


def refresh_knowledge_base() -> str:
    """Rebuild the vector store using the existing ingestion pipeline."""
    os.makedirs("uploads", exist_ok=True)
    result = subprocess.run(
        [sys.executable, "src/ingest.py"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout + result.stderr
