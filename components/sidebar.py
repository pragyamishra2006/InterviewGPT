"""Sidebar navigation and persistent workspace controls."""

from __future__ import annotations

import os

import streamlit as st


def render_sidebar() -> None:
    """Render the premium sidebar with navigation and workspace tools."""
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-card">
                <div class="sidebar-brand">🤖 InterviewGPT</div>
                <div class="sidebar-subtitle">Premium AI interview prep workspace</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("＋ New Chat", use_container_width=True):
            st.session_state.page = "Chat"
            st.session_state.current_chat_id = None
            st.session_state.messages = []

        nav_items = [
            ("Home", "🏠"),
            ("Chat", "💬"),
            ("Upload", "📤"),
            ("Mock Interview", "🎤"),
            ("Resume", "📄"),
            ("Settings", "⚙️"),
        ]
        for label, icon in nav_items:
            is_active = st.session_state.page == label
            button_label = f"{icon} {label}"
            if st.button(
                button_label,
                key=f"sidebar_{label.lower().replace(' ', '_')}",
                use_container_width=True,
            ):
                st.session_state.page = label
            if is_active:
                st.markdown("<div class='nav-active'></div>", unsafe_allow_html=True)

        st.markdown("### Conversation History")
        chat_history = st.session_state.get("chat_history", [])
        if chat_history:
            for chat in chat_history:
                if st.button(
                    chat["title"],
                    key=f"chat_{chat['id']}",
                    use_container_width=True,
                ):
                    st.session_state.current_chat_id = chat["id"]
                    st.session_state.messages = chat.get("messages", [])
                    st.session_state.page = "Chat"
        else:
            st.info("No conversations yet.")

        st.markdown("### Uploaded Documents")
        uploads = [
            f for f in os.listdir("uploads") if f.lower().endswith(".pdf")
        ]
        if uploads:
            for file_name in uploads:
                st.write(f"📄 {file_name}")
        else:
            st.caption("Upload PDFs to enrich your knowledge base")

        st.markdown("---")
        st.markdown("### Workspace")
        if st.button("🗑 Delete Documents", use_container_width=True):
            for file_name in uploads:
                os.remove(os.path.join("uploads", file_name))
            st.success("Knowledge base cleared.")

        if st.button("📝 Rename Chat", use_container_width=True):
            st.session_state.rename_requested = True

        if st.session_state.get("rename_requested"):
            new_title = st.text_input("New title", key="rename_title")
            if st.button("Save", key="save_rename"):
                if new_title:
                    for chat in st.session_state.chat_history:
                        if chat["id"] == st.session_state.current_chat_id:
                            chat["title"] = new_title
                            break
                st.session_state.rename_requested = False

        st.markdown("---")
        st.markdown(
            """
            <div class="profile-card">
                <div class="profile-avatar">AI</div>
                <div>
                    <div class="profile-name">AI Copilot</div>
                    <div class="profile-role">Ready to help</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        storage_pct = min(100, max(18, len(uploads) * 24 + 25))
        st.progress(storage_pct / 100)
        st.caption(f"Storage ready • {len(uploads)} PDFs indexed")

        if st.button("🌙 Toggle Theme", use_container_width=True):
            st.session_state.theme = (
                "light" if st.session_state.theme == "dark" else "dark"
            )
            st.rerun()
