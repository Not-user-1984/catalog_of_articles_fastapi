import asyncio
import os
from typing import AsyncGenerator
from src.config import settings
import asyncpg
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from database import cleanup_database, engine_test, get_async_session_test_db, upgrade_database
from src.db.database import Base, metadata
from src.db.database import get_async_session
from src.main import app


# metadata.bind = engine_test

# app.dependency_overrides[get_async_session] = get_async_session_test_db


# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     async with engine_test.begin() as conn:
#         await conn.run_sync(metadata.create_all)
#         print(Base.metadata)
#     yield
#
#     async with engine_test.begin() as conn:
#         print(metadata)
#         await conn.run_sync(metadata.drop_all)

# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     # Примените миграции
#     await upgrade_database()
#
#     yield
#
#     # Удалите таблицы
#     await cleanup_database()

@pytest.fixture()
async def session_db():
    connect = await asyncpg.connect(settings.DATABASE_URL_TEST)
    yield connect
    await connect.close()


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="function")
async def fastapi_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
