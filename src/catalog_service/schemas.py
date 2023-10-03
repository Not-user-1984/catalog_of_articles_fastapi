from pydantic import BaseModel

from typing import List


class UserArticle(BaseModel):
    user_id: int
    article_id: int


class ArticleCategoryCreate(BaseModel):
    name: str


class ArticleCategoryUpdate(BaseModel):
    name: str


class ArticleCategory(ArticleCategoryCreate):
    id: int


class ArticleCreate(BaseModel):
    title: str
    description: str
    link: str
    category_id: int


class ArticleUpdate(BaseModel):
    title: str
    description: str
    link: str


class Article(ArticleCreate):
    id: int
    category: str
    author: str


class ArticleCategoryRequest(ArticleCategoryCreate):
    pass


class ArticleCategoryResponse(ArticleCategory):
    pass


class ArticleRequest(ArticleCreate):
    pass


class ArticleResponse(Article):
    authors: List[UserArticle]

