from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
        APP_NAME: str = "DevOps Copilot"
        APP_VERSION: str = "0.1.0"
        HOST: str = "0.0.0.0"
        PORT: int = 8000

        model_config = SettingsConfigDict(
            env_file=".env",
            case_sensitive=True,
        )

settings = Settings()
