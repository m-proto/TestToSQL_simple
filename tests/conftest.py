"""Configuration pytest commune pour tous les tests"""

import pytest
from unittest.mock import Mock, patch, MagicMock


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Configuration globale de Streamlit pour les tests"""
    # Mock des colonnes
    mock_col = MagicMock()
    mock_columns = Mock(return_value=[mock_col, mock_col])

    # Mock du context manager sidebar
    mock_sidebar = MagicMock()
    mock_sidebar.__enter__ = Mock()
    mock_sidebar.__exit__ = Mock()

    # Mock du context manager spinner
    mock_spinner = MagicMock()
    mock_spinner.__enter__ = Mock()
    mock_spinner.__exit__ = Mock()

    # Configuration de base de session_state
    session_state = {
        "language": "fr",
        "translations": {
            "test_key": "Valeur de test",
            "app_title": "Test App",
            "generating": "Génération...",
            "error_generation": "Erreur",
            "sql_generated": "SQL généré",
            "select_language": "Sélectionner la langue",
            "database_config": "Configuration BDD",
            "llm_settings": "Paramètres LLM",
            "system_title": "Informations système",
        },
    }

    # Patch multiple des fonctions Streamlit
    with patch.multiple(
        "streamlit",
        session_state=session_state,
        sidebar=Mock(return_value=mock_sidebar),
        columns=mock_columns,
        spinner=Mock(return_value=mock_spinner),
        markdown=Mock(),
        error=Mock(),
        success=Mock(),
        subheader=Mock(),
        selectbox=Mock(),
        metric=Mock(),
        caption=Mock(),
        button=Mock(),
    ):
        yield
