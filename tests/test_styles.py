"""Tests de smoke pour les styles"""

from unittest.mock import patch
from ui.styles.themes import load_custom_css


@patch("streamlit.markdown")
def test_load_custom_css_smoke(mock_markdown):
    """Vérifie que le chargement du CSS ne lève pas d'erreur"""
    load_custom_css()
    mock_markdown.assert_called_once()
