"""Settings page for theme, font, model, and retrieval tuning."""

from __future__ import annotations

import streamlit as st


def render_settings_page() -> None:
    """Render controls that tailor the UI and retrieval behavior."""
    st.markdown("## ⚙️ Workspace Settings")
    st.caption("Fine-tune the experience to match your study flow")

    theme = st.selectbox("Theme", ["Dark", "Light"], index=0)
    st.select_slider(
        "Font Size",
        options=["Small", "Medium", "Large"],
        value="Medium",
    )
    model = st.selectbox(
        "Model",
        ["qwen2.5:1.5b", "llama3.2", "mistral"],
        index=0,
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.2)
    top_k = st.slider("Top-K Retrieval", 2, 8, 4)

    st.session_state.theme = theme.lower()
    st.session_state.model = model
    st.session_state.temperature = temperature
    st.session_state.top_k = top_k

    st.info(
        "These settings are wired into the app state and can be expanded "
        "into persisted profiles."
    )
