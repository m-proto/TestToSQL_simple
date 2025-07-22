"""
Pied de page de l'application
"""

import streamlit as st
from langue.translator import get_text


def render_footer():
    """Affiche le pied de page"""

    # CSS pour le footer
    st.markdown(
        """
    <style>
    .footer {
        margin-top: 3rem;
        padding: 2rem 0;
        border-top: 2px solid #e0e0e0;
        text-align: center;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
    }
    .footer-content {
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
    }
    .footer-section {
        margin: 0.5rem;
    }
    .footer-link {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
    }
    .footer-link:hover {
        text-decoration: underline;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Contenu du footer
    st.markdown("---")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("**🔄 v1.0.0 | TextToSQL**")

    with col2:
        st.markdown(
            f"""
        <div style='text-align: right;'>
            <p><small>{get_text('powered_by')} <strong>Streamlit</strong> + <strong>LangChain</strong> + <strong>Google Gemini</strong></small></p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Copyright
    st.markdown(
        """
    <div style='text-align: center; margin-top: 1rem; color: #666;'>
        <small>© Text-to-SQL 2025 – DS Team. [PROTO] MAMADOU.</small>
    </div>
    """,
        unsafe_allow_html=True,
    )
