from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from db.models import ArticleCategory, Article, UserArticle, User


async def validate_category_name(db: AsyncSession, name: str):
    existing_category = await db.execute(
        select(ArticleCategory).where(ArticleCategory.name == name)
    )

    if existing_category.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Category with the same name already exists"
        )
