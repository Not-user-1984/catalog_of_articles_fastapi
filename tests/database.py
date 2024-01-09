from typing import AsyncGenerator
from alembic.config import Config
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from alembic import command
from src.config import settings
from src.db.models import Base

alembic_cfg = Config("alembic.ini")

engine_test = create_async_engine(
    settings.DATABASE_URL_TEST, poolclass=NullPool)

async_session_maker_test = sessionmaker(
    engine_test,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session_test_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker_test() as session:
        yield session


async def upgrade_database():
    # Примените все миграции
    await command.upgrade(alembic_cfg, "head")


async def downgrade_database():
    # Откат до начального состояния базы данных
    await command.downgrade(alembic_cfg, "base")


async def cleanup_database():
    async with AsyncSession(engine_test) as session:
        async with session.begin() as conn:
            # Удалите таблицы
            for table in reversed(Base.metadata.sorted_tables):
                await conn.run_sync(table.drop)
