from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings
from logging_sys import logger

try:
    logger.info("Initializing database engine...")

    engine = create_async_engine(
        str(settings.pg_dsn),
        echo=True,  # SET TRUE FOR ONLY DEBUG
        pool_size=5,
        max_overflow=2,
    )
    AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

    logger.success("Database engine initialized successfully.")

except Exception as e:
    logger.error(f"Failed to initialize database engine: {e}")
    raise
