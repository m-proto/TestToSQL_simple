"""
Gestion robuste des connexions Redshift avec retry et pooling
Compatible avec LLMManagerSQLChain (utilise uniquement le SQLAlchemy Engine)
"""

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy import inspect
from tenacity import retry, stop_after_attempt, wait_exponential
from infrastructure.settings import settings
from infrastructure.logging import logger


class DatabaseManager:
    def __init__(self):
        self.engine: Engine | None = None
        self._connect()

    @retry(
        stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=2, max=5)
    )
    def _connect(self):
        """Établit la connexion Redshift avec pooling et retry"""
        try:
            logger.info(
                "Connecting to Redshift",
                host=settings.redshift_host,
                database=settings.redshift_db,
                schema=settings.redshift_schema,
            )

            # Création du moteur SQLAlchemy avec configuration robuste
            self.engine = create_engine(
                settings.redshift_dsn,
                poolclass=QueuePool,
                pool_size=settings.db_pool_size,
                max_overflow=settings.db_pool_overflow,
                pool_timeout=10,
                pool_pre_ping=True,
                pool_recycle=3600,
                echo=settings.debug,
                connect_args={
                    "connect_timeout": 8,
                    "application_name": "TextToSQL_Streamlit",
                },
            )

            # Test simple de connectivité
            with self.engine.connect() as conn:
                conn.execute("SELECT 1")

            # Introspection des tables (log des 5 premières)
            inspector = inspect(self.engine)
            tables = inspector.get_table_names(schema=settings.redshift_schema)
            logger.info(
                "Database connection successful",
                tables_count=len(tables),
                tables=tables[:5],
            )

        except Exception as e:
            logger.error(
                "Database connection failed", error=str(e), host=settings.redshift_host
            )
            raise

    def health_check(self) -> bool:
        """Vérifie la santé de la connexion"""
        try:
            with self.engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            logger.error("Database health check failed", error=str(e))
            return False

    def close(self):
        """Ferme proprement les connexions"""
        if self.engine:
            self.engine.dispose()
            logger.info("Database connections closed")


# Instance globale (singleton)
db_manager = DatabaseManager()


def connect_to_redshift() -> Engine:
    """Expose le moteur SQLAlchemy Redshift (utilisé par LLMManagerSQLChain)"""
    return db_manager.engine
