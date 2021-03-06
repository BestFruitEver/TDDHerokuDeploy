import logging
import os
from typing import Set
from pydantic import BaseSettings, AnyUrl
from functools import lru_cache

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT","dev")
    testing: bool = os.getenv("TESTING",0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Chargement des paramètres de l'environnement...")
    return Settings()
