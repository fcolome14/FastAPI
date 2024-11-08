from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path
    
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int 
    
    #NOTE: Names must match the ones in .env file

    class Config:
        env_file = os.path.join(Path(__file__).resolve().parent.parent, ".env")

settings = Settings()