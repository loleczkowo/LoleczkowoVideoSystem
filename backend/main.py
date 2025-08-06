from logging_sys import logger, enable_ansi

enable_ansi()  # enables colored text

from fastapi import FastAPI                     # noqa: E402
from contextlib import asynccontextmanager      # noqa: E402

from app.models import Base                     # noqa: E402
from app.db import engine                       # noqa: E402
from app.routers import all_routers             # noqa: E402


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting...")

    try:
        logger.info("Connecting to database...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.success("Started")
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise

    yield

    logger.info("Shutting down...")
    # No explicit shutdown needed here
    logger.success("Shutdown complete.")


app = FastAPI(title="LVS API", lifespan=lifespan)

for router in all_routers:
    app.include_router(router)
