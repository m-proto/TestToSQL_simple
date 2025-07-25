import pytest
from unittest.mock import Mock, patch, MagicMock


@pytest.fixture(autouse=True)
def disable_retry(monkeypatch):
    """Désactive le retry de tenacity pour les tests"""

    def mock_retry(*args, **kwargs):
        def decorator(func):
            return func

        return decorator

    monkeypatch.setattr("infrastructure.database.retry", mock_retry)


@pytest.fixture
def mock_inspector():
    """Fixture pour mocker l'inspecteur SQLAlchemy"""
    inspector = Mock()
    inspector.get_table_names.return_value = ["table1", "table2"]
    return inspector


@pytest.fixture
def mock_engine(mock_inspector):
    """Fixture pour mocker le SQLAlchemy Engine"""
    engine = Mock()
    connection = MagicMock()
    connection.execute.return_value = True
    engine.connect.return_value = connection
    return engine


@pytest.fixture
def mock_create_engine(mock_engine):
    """Fixture pour mocker create_engine"""
    with patch(
        "infrastructure.database.create_engine", return_value=mock_engine
    ) as mock:
        yield mock


@pytest.fixture(autouse=True)
def mock_inspect(mock_inspector):
    """Fixture pour mocker la fonction inspect de SQLAlchemy"""
    with patch("infrastructure.database.inspect", return_value=mock_inspector):
        yield


def test_database_manager_init(mock_create_engine, mock_engine):
    """Test l'initialisation simple du DatabaseManager"""
    from infrastructure.database import DatabaseManager

    db = DatabaseManager()
    assert db.engine == mock_engine
    mock_create_engine.assert_called_once()


def test_health_check_success(mock_create_engine, mock_engine):
    """Test un health check réussi"""
    from infrastructure.database import DatabaseManager

    db = DatabaseManager()
    assert db.health_check() is True


def test_health_check_failure(mock_create_engine, mock_engine):
    """Test un health check échoué"""
    from infrastructure.database import DatabaseManager

    # Créer d'abord l'instance avec une connexion réussie
    db = DatabaseManager()
    # Puis simuler une erreur pour le health check
    mock_engine.connect.side_effect = Exception("Health check failed")
    assert db.health_check() is False
