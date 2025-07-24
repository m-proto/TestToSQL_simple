import os
import streamlit as st
from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Optional
from dotenv import load_dotenv

# 1. Charger .env localement
load_dotenv()

# 2. Fallback sécurisé pour Streamlit Cloud
try:
    for key, value in st.secrets.items():
        os.environ[key.upper()] = str(value)
except Exception:
    pass


# 3. Config Pydantic
class Settings(BaseSettings):
    redshift_user: str
    redshift_password: str
    redshift_host: str
    redshift_port: int = 5439
    redshift_db: str
    redshift_schema: str = "public"
    google_api_key: str

    app_name: str = "TextToSQL"
    app_version: str = "1.0.0"
    debug: bool = False

    db_pool_size: int = 10
    db_pool_overflow: int = 20
    db_pool_timeout: int = 30

    rate_limit_requests: int = 100
    rate_limit_window: int = 3600

    redis_url: Optional[str] = None
    cache_ttl: int = 3600

    log_level: str = "INFO"
    log_format: str = "json"

    @field_validator("redshift_port")
    @classmethod
    def validate_port(cls, v):
        if not 1 <= v <= 65535:
            raise ValueError("Port must be between 1 and 65535")
        return v

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in levels:
            raise ValueError(f"Log level must be one of {levels}")
        return v.upper()

    @property
    def redshift_dsn(self) -> str:
        return (
            f"redshift+psycopg2://{self.redshift_user}:{self.redshift_password}"
            f"@{self.redshift_host}:{self.redshift_port}/{self.redshift_db}"
        )

    model_config = {
        "env_file": ".env",
        "env_prefix": "",
        "case_sensitive": False,
        "extra": "ignore",
    }


# 4. Instance globale
settings = Settings()
