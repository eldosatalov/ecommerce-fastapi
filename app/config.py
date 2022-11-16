from logging import getLogger
import os
from functools import lru_cache

from pydantic import BaseSettings


logger = getLogger(__name__)


class Settings(BaseSettings):
    DB_USER = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    DB_NAME = os.getenv("POSTGRES_DB", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


@lru_cache
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()
