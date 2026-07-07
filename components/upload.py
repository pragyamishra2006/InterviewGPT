"""Upload experience with drag-and-drop, validation, and progress feedback."""

from __future__ import annotations

import os
from pathlib import Path

import streamlit as st

from utils.rag import refresh_knowledge_base


def render_upload_page() -> None:
    """Render the polished upload experience."""
    st.markdown("## 📤 Knowledge Base Manager")
    st.caption(
        "Upload multiple PDFs and refresh your retrieval index instantly"
    )

    uploaded_files = st.file_uploader(
        "Upload one or more PDF documents",
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_uploader",
    )

    if uploaded_files:
        progress_bar = st.progress(0)
        uploaded_count = 0
        for index, uploaded_file in enumerate(uploaded_files, start=1):
            destination = Path("uploads") / uploaded_file.name
            if destination.exists():
                st.warning(f"Skipped duplicate: {uploaded_file.name}")
                continue
            with open(destination, "wb") as handle:
                handle.write(uploaded_file.getbuffer())
            uploaded_count += 1
            progress_bar.progress(index / len(uploaded_files))
        if uploaded_count:
            st.success(f"Saved {uploaded_count} new PDF(s) to your workspace.")
            with st.spinner("Rebuilding embeddings..."):
                status = refresh_knowledge_base()
            st.success("Knowledge base refreshed successfully.")
            st.code(status[:1000], language="text")

    st.markdown("#### Knowledge Base Statistics")
    pdf_files = [
        f for f in os.listdir("uploads") if f.lower().endswith(".pdf")
    ]
    st.metric("Total Documents", len(pdf_files))
    st.metric("Embedding Status", "Ready" if pdf_files else "Pending")
    st.metric("Total Chunks", "Available after ingestion")
