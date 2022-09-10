import pathlib

from pydantic import BaseSettings

APP_PATH = pathlib.Path(__file__).parent


class Settings(BaseSettings):
    DEBUG: bool = False
    SQL_TAP: bool = False

    class Config:
        case_sensitive = True
        env_file = APP_PATH / '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
