import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str

    class Config:
        env_file = ".env"


config = Settings(_env_file=f"{str(os.environ.get('ENV_FILE_PREFIX') or '')}.env")