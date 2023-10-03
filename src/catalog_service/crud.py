from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from db.models import ArticleCategory, Article, UserArticle, User

from . import schemas


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


async def get_article_category(db: AsyncSession, category_id: int):
    category = await db.execute(
        select(ArticleCategory).where(ArticleCategory.id == category_id)
    )
    return category.scalar_one_or_none()


async def get_article_categories(db: AsyncSession):
    categories = await db.execute(select(ArticleCategory))
    return categories.scalars().all()


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


async def delete_article_category(db: AsyncSession, category_id: int):
    db_category = await get_article_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category


async def create_article(
        db: AsyncSession,
        article: schemas.ArticleCreate,
        user_id: int):

    db_article = Article(
        **article.dict(),
        authors=[UserArticle(user_id=user_id)])
    db.add(db_article)
    await db.commit()
    return db_article


async def get_article(db: AsyncSession, article_id: int):
    article = await db.execute(
        select(Article).where(Article.id == article_id)
    )
    return article.scalar_one_or_none()


async def get_articles(db: AsyncSession,
                       skip: int = 0,
                       limit: int = 10
                       ):
    articles = await db.execute(
        select(
            Article,
            User.username,
            ArticleCategory.name)
        .offset(skip)
        .limit(limit)
    )
    result = articles.all()

    articles_with_names = [
        {
            "id": article.id,
            "title": article.title,
            "description": article.description,
            "link": article.link,
            "created_at": article.created_at,
            "updated_at": article.updated_at,
            "category_id": article.category_id,
            "category": name,
            "author": username
        }
        for article, username, name in result
    ]

    return articles_with_names


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


async def delete_article(db: AsyncSession, article_id: int):
    db_article = await get_article(db, article_id)
    if db_article:
        await db.delete(db_article)
        await db.commit()
    return db_article
