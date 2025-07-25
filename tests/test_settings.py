import pytest
from pydantic import ValidationError
from infrastructure.settings import Settings


@pytest.fixture
def mock_env(monkeypatch):
    """Fixture pour mocker les variables d'environnement"""
    env_vars = {
        "REDSHIFT_USER": "test_user",
        "REDSHIFT_PASSWORD": "test_pass",
        "REDSHIFT_HOST": "test.host.com",
        "REDSHIFT_PORT": "5439",
        "REDSHIFT_DB": "test_db",
        "GOOGLE_API_KEY": "test_api_key",
    }
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)
    return env_vars


def test_settings_basic(mock_env):
    """Test la création basique des settings"""
    settings = Settings()
    assert settings.redshift_user == "test_user"
    assert settings.redshift_password == "test_pass"
    assert settings.redshift_host == "test.host.com"
    assert settings.redshift_port == 5439
    assert settings.redshift_db == "test_db"
    assert settings.google_api_key == "test_api_key"


def test_settings_defaults():
    """Test les valeurs par défaut"""
    settings = Settings(
        redshift_user="user",
        redshift_password="pass",
        redshift_host="host",
        redshift_db="db",
        google_api_key="key",
    )
    assert settings.redshift_schema == "usedcar_dwh"  # Valeur correcte du schéma
    assert settings.app_name == "TextToSQL"
    assert settings.debug is True  # Valeur correcte de debug
    assert settings.db_pool_size == 10
    assert settings.cache_ttl == 3600
    assert settings.log_level == "INFO"


def test_redshift_dsn(mock_env):
    """Test la génération du DSN Redshift"""
    settings = Settings()
    expected_dsn = "redshift+psycopg2://test_user:test_pass@test.host.com:5439/test_db"
    assert settings.redshift_dsn == expected_dsn


def test_invalid_port():
    """Test la validation du port"""
    with pytest.raises(ValidationError) as exc_info:
        Settings(
            redshift_user="user",
            redshift_password="pass",
            redshift_host="host",
            redshift_port=70000,  # Port invalide
            redshift_db="db",
            google_api_key="key",
        )
    assert "Port must be between 1 and 65535" in str(exc_info.value)


def test_invalid_log_level():
    """Test la validation du niveau de log"""
    with pytest.raises(ValidationError) as exc_info:
        Settings(
            redshift_user="user",
            redshift_password="pass",
            redshift_host="host",
            redshift_db="db",
            google_api_key="key",
            log_level="INVALID",  # Niveau de log invalide
        )
    assert "Log level must be one of" in str(exc_info.value)
