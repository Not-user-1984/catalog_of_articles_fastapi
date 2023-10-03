from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from . import crud
from . import schemas

router = APIRouter()

# Создать категорию статьи
@router.post("/article_categories/", response_model=schemas.ArticleCategory)
async def create_article_category_endpoint(
    category: schemas.ArticleCategoryCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_article_category(db, category)

# Получить категорию статьи по ID
@router.get("/article_categories/{category_id}", response_model=schemas.ArticleCategory)
async def read_article_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.get_article_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Article Category not found")
    return category

# Получить список всех категорий статей
@router.get("/article_categories/", response_model=list[schemas.ArticleCategory])
async def read_article_categories_endpoint(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_article_categories(db)

# Обновить информацию о категории статьи
@router.put("/article_categories/{category_id}", response_model=schemas.ArticleCategory)
async def update_article_category_endpoint(
    category_id: int,
    category_data: schemas.ArticleCategoryUpdate,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.update_article_category(db, category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Article Category not found")
    return category

# Удалить категорию статьи
@router.delete("/article_categories/{category_id}", response_model=schemas.ArticleCategory)
async def delete_article_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    category = await crud.delete_article_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Article Category not found")
    return category

# Создать статью
@router.post("/articles/", response_model=schemas.Article)
async def create_article_endpoint(
    article: schemas.ArticleCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_article(db, article)

# Получить статью по ID
@router.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article_endpoint(
    article_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    article = await crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

# Получить список всех статей
@router.get("/articles/", response_model=list[schemas.Article])
async def read_articles_endpoint(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_articles(db)

# Обновить информацию о статье
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

# Удалить статью
@router.delete("/articles/{article_id}", response_model=schemas.Article)
async def delete_article_endpoint(
    article_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    article = await crud.delete_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
