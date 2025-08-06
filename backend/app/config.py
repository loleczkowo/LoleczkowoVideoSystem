from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
import os


class Settings(BaseSettings):
    pg_dsn: PostgresDsn

    class Config:
        env_prefix = "LVS_"
        env_file = os.path.join(os.path.dirname(__file__), "..", "backend.env")


settings = Settings()
