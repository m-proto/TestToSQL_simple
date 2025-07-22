import logging
from sqlalchemy.engine import Engine
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from infrastructure.settings import settings

logger = logging.getLogger(__name__)


def get_gemini_llm() -> BaseChatModel:
    """
    Initialise et retourne un modèle Gemini avec API Key.
    """
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", temperature=0, google_api_key=settings.google_api_key
    )


def get_sql_db(engine: Engine) -> SQLDatabase:
    """
    Initialise SQLDatabase avec le schéma utilisé.
    """
    return SQLDatabase(engine, schema="usedcar_dwh")


def create_sql_query_chain_only(llm: BaseChatModel, db: SQLDatabase):
    """
    Crée un SQL Query Chain qui génère du SQL uniquement (sans exécution).
    """
    return create_sql_query_chain(llm, db)
