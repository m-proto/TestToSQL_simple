import pytest
from unittest.mock import Mock, patch
from infrastructure.llm import get_gemini_llm, get_sql_db, create_sql_query_chain_only

@pytest.fixture
def mock_llm():
    """Fixture pour mocker le modèle LLM"""
    mock = Mock()
    return mock

def test_get_gemini_llm():
    """Test la création du modèle Gemini"""
    with patch("infrastructure.llm.ChatGoogleGenerativeAI") as mock_gemini:
        llm = get_gemini_llm()
        assert llm is not None
        assert mock_gemini.called

def test_get_sql_db():
    """Test la création de SQLDatabase"""
    mock_engine = Mock()
    with patch("infrastructure.llm.SQLDatabase") as mock_sql_db:
        db = get_sql_db(mock_engine)
        assert db is not None
        mock_sql_db.assert_called_once()

def test_create_sql_query_chain_only():
    """Test la création de la chaîne SQL"""
    mock_llm = Mock()
    mock_db = Mock()
    with patch("infrastructure.llm.create_sql_query_chain") as mock_create_chain:
        chain = create_sql_query_chain_only(mock_llm, mock_db)
        assert chain is not None
        mock_create_chain.assert_called_once_with(mock_llm, mock_db) 