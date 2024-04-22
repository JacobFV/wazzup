from pydantic import BaseSettings

class Settings(BaseSettings):
    # Define configuration settings
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expiration_minutes: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
