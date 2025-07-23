import logging
from sqlalchemy.engine import Engine
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.prompts import PromptTemplate
from infrastructure.settings import settings
from infrastructure.prompts import PROMPT_TEMPLATE_EN
 

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
    Crée un SQL Query Chain qui génère du SQL uniquement (version standard).
    """
    return create_sql_query_chain(llm, db)


def create_custom_sql_query_chain(llm: BaseChatModel) -> LLMChain:
    """
    Crée une chaîne LLM avec un prompt personnalisé pour générer du SQL.
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template=PROMPT_TEMPLATE_EN,
    )
    return LLMChain(llm=llm, prompt=prompt)
