from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from db.models import ArticleCategory, Article

from . import schemas


# Создать категорию статьи
async def create_article_category(
        db: AsyncSession,
        category: schemas.ArticleCategoryCreate):
    existing_category = await db.execute(
        select(ArticleCategory).where(ArticleCategory.name == category.name)
    )
    if existing_category.scalar_one_or_none():
        raise HTTPException(
            status_code=409,
            detail="Article category with the same name already exists"
        )
    db_category = ArticleCategory(**category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


# Получить категорию статьи по ID
async def get_article_category(db: AsyncSession, category_id: int):
    category = await db.execute(
        select(ArticleCategory).where(ArticleCategory.id == category_id)
    )
    return category.scalar_one_or_none()


# Получить список всех категорий статей
async def get_article_categories(db: AsyncSession):
    categories = await db.execute(select(ArticleCategory))
    return categories.scalars().all()


# Обновить информацию о категории статьи
async def update_article_category(
        db: AsyncSession,
        category_id: int,
        category_data: schemas.ArticleCategory):
    db_category = await get_article_category(db, category_id)
    if db_category:
        for field, value in category_data.dict().items():
            setattr(db_category, field, value)
        await db.commit()
        await db.refresh(db_category)
    return db_category


# Удалить категорию статьи
async def delete_article_category(db: AsyncSession, category_id: int):
    db_category = await get_article_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category


# Создать статью
async def create_article(
        db: AsyncSession,
        article: schemas.ArticleCreate):

    db_article = Article(**article.dict())
    db.add(db_article)
    await db.commit()
    await db.refresh(db_article)
    return db_article


# Получить статью по ID
async def get_article(db: AsyncSession, article_id: int):
    article = await db.execute(
        select(Article).where(Article.id == article_id)
    )
    return article.scalar_one_or_none()


# Получить список всех статей
async def get_articles(db: AsyncSession):
    articles = await db.execute(select(Article))
    return articles.scalars().all()


# Обновить информацию о статье
async def update_article(
        db: AsyncSession,
        article_id: int,
        article_data: schemas.Article):
    db_article = await get_article(db, article_id)
    if db_article:
        for field, value in article_data.dict().items():
            setattr(db_article, field, value)
        await db.commit()
        await db.refresh(db_article)
    return db_article


# Удалить статью
async def delete_article(db: AsyncSession, article_id: int):
    db_article = await get_article(db, article_id)
    if db_article:
        await db.delete(db_article)
        await db.commit()
    return db_article
