from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from . import crud
from . import schemas
from . import validation
from db.models import User
from auth.routers import curred_user
router = APIRouter()


@router.post(
        "/article_categories/",
        response_model=schemas.ArticleCategory
        )
async def create_article_category_endpoint(
    category: schemas.ArticleCategoryCreate,
    db: AsyncSession = Depends(get_async_session)
):
    await validation.validate_category_name(db, category.name)
    return await crud.create_article_category(db, category)


@router.get("/article_categories/{category_id}",
            response_model=schemas.ArticleCategory)
async def read_article_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.get_article_category(db, category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Article Category not found")
    return category


@router.get("/article_categories/",
            response_model=list[schemas.ArticleCategory])
async def read_article_categories_endpoint(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_article_categories(db)


@router.put("/article_categories/{category_id}",
            response_model=schemas.ArticleCategory)
async def update_article_category_endpoint(
    category_id: int,
    category_data: schemas.ArticleCategoryUpdate,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.update_article_category(
        db, category_id, category_data)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Article Category not found")
    return category


@router.delete(
        "/article_categories/{category_id}",
        response_model=schemas.ArticleCategory)
async def delete_article_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.delete_article_category(db, category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Article Category not found")
    return category


@router.post("/articles/", response_model=schemas.ArticleResponse)
async def create_article_endpoint(
    article: schemas.ArticleCreate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(curred_user),
):
    return await crud.create_article(db, article, user.id)


@router.get("/articles/{article_id}",
            response_model=schemas.Article
            )
async def read_article_endpoint(
    article_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    article = await crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.get("/articles/", response_model=list[schemas.Article])
async def read_articles_endpoint(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_articles(db)


@router.put("/articles/{article_id}", response_model=schemas.Article)
async def update_article_endpoint(
    article_id: int,
    article_data: schemas.ArticleUpdate,
    db: AsyncSession = Depends(get_async_session)
):
    article = await crud.update_article(db, article_id, article_data)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.delete("/articles/{article_id}", response_model=schemas.Article)
async def delete_article_endpoint(
    article_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    article = await crud.delete_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
