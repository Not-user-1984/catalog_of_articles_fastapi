import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Fast api"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db")
    DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}?async_fallback=True"

    DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
    DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
    DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
    DB_USER_TEST = os.environ.get("DB_USER_TEST")
    DB_PASS_TEST = os.environ.get("DB_PASS_TEST")
    DATABASE_URL_TEST: str = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}?async_fallback=True"

    app_title: str = 'catalog_of_articles_fastapi'
    description: str = 'catalog_of_articles_fastapi'
    SECRET_AUTH: str = os.getenv("SECRET_AUTH", "hjhjhfg131425ubjbjb")


settings = Settings()
