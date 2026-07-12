from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ------------------------
    # Application Constants
    # ------------------------

    APP_NAME: str = "Image Search Platform API"
    APP_VERSION: str = "2.0.0"
    API_PREFIX: str = "/api/v1"

    # ------------------------
    # Environment Variables
    # ------------------------

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    FRONTEND_URL: str
    BACKEND_URL: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()