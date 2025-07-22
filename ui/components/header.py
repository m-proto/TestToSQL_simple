"""
En-tête de l'application Streamlit
"""

import streamlit as st
from langue.translator import get_text


def render_header():
    """Affiche l'en-tête principal de l'application"""

    # CSS pour l'en-tête
    st.markdown(
        """
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .header-divider {
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
        border: none;
        margin: 2rem 0;
        border-radius: 2px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # En-tête principal
    st.markdown(
        f"""
    <div class="main-header">
        <h1>🔄 {get_text('app_title')}</h1>
        <p>{get_text('app_subtitle')}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Divider décoratif
    st.markdown('<hr class="header-divider">', unsafe_allow_html=True)


def render_navigation():
    """Affiche la navigation par onglets"""
    tabs = st.tabs(
        [get_text("tab_generator"), get_text("tab_history"), get_text("tab_settings")]
    )
    return tabs
