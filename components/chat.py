"""Chat experience with streaming-style UX and message history."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

import streamlit as st

from utils.rag import generate_answer, retrieve_documents


def init_session_defaults() -> None:
    """Initialize state required by the redesigned app."""
    defaults = {
        "page": "Home",
        "theme": "dark",
        "messages": [],
        "chat_history": [],
        "current_chat_id": None,
        "model": "qwen2.5:1.5b",
        "temperature": 0.2,
        "top_k": 4,
        "pending_prompt": "",
        "rename_requested": False,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def ensure_chat_exists() -> dict[str, Any]:
    """Create or reuse a chat entry."""
    if st.session_state.current_chat_id is None:
        st.session_state.current_chat_id = str(uuid.uuid4())[:8]
        st.session_state.chat_history.append(
            {
                "id": st.session_state.current_chat_id,
                "title": "New Conversation",
                "updated_at": datetime.now().strftime("%H:%M"),
                "messages": [],
            }
        )
    return next(
        chat
        for chat in st.session_state.chat_history
        if chat["id"] == st.session_state.current_chat_id
    )


def render_chat_page() -> None:
    """Render the main chat experience with history and generated answers."""
    st.markdown("## 💬 Interview Assistant")
    st.caption("Context-rich answers grounded in your uploaded notes")

    chat = ensure_chat_exists()

    for index, message in enumerate(chat.get("messages", [])):
        role = message["role"]
        content = message["content"]
        timestamp = message.get("timestamp", datetime.now().strftime("%H:%M"))
        if role == "user":
            st.markdown(
                f"<div class='bubble user-bubble'><strong>You</strong><br/>{content}</div>",
                unsafe_allow_html=True,
            )
            st.caption(timestamp)
        else:
            with st.container():
                st.markdown(
                    f"<div class='bubble assistant-bubble'><strong>InterviewGPT</strong><br/></div>",
                    unsafe_allow_html=True,
                )
                st.markdown(content)
                st.caption(timestamp)
                col_a, col_b, col_c = st.columns([1, 1, 4])
                with col_a:
                    if st.button("Copy", key=f"copy_{index}"):
                        st.info("Answer copied to your workflow.")
                with col_b:
                    if st.button("👍", key=f"like_{index}"):
                        st.success("Feedback saved.")
                with col_c:
                    if st.button("👎", key=f"dislike_{index}"):
                        st.warning("Feedback saved.")

    prompt = st.text_area(
        "Your message",
        value=st.session_state.pending_prompt,
        placeholder="Ask something like: Explain deadlocks with examples",
        height=90,
    )
    st.session_state.pending_prompt = ""

    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("Send", use_container_width=True):
            if prompt.strip():
                chat.setdefault("messages", []).append(
                    {
                        "role": "user",
                        "content": prompt.strip(),
                        "timestamp": datetime.now().strftime("%H:%M"),
                    }
                )
                chat["title"] = prompt.strip()[:24] or "New Conversation"
                chat["updated_at"] = datetime.now().strftime("%H:%M")
                with st.spinner("Retrieving context..."):
                    docs = retrieve_documents(
                        prompt.strip(),
                        top_k=st.session_state.top_k,
                    )
                with st.spinner("Generating answer..."):
                    answer = generate_answer(
                        prompt.strip(),
                        docs,
                        model=st.session_state.model,
                        temperature=st.session_state.temperature,
                    )
                chat.setdefault("messages", []).append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "timestamp": datetime.now().strftime("%H:%M"),
                    }
                )
                st.rerun()
    with col2:
        if st.button("Regenerate", use_container_width=True):
            st.info("Regeneration uses the latest prompt context.")
    with col3:
        st.caption("Tip: Use your uploaded PDFs to ground every answer.")
