from pydantic import BaseModel


# Схема для создания категории статьи
class ArticleCategoryCreate(BaseModel):
    name: str


# Схема для обновления категории статьи
class ArticleCategoryUpdate(BaseModel):
    name: str


# Схема для категории статьи
class ArticleCategory(ArticleCategoryCreate):
    id: int


# Схема для создания статьи
class ArticleCreate(BaseModel):
    title: str
    description: str
    link: str
    category_id: int


# Схема для обновления статьи
class ArticleUpdate(BaseModel):
    title: str
    description: str
    link: str


# Схема для статьи
class Article(ArticleCreate):
    id: int


# Схемы для запросов и ответов CRUD операций с категорией статьи
class ArticleCategoryRequest(ArticleCategoryCreate):
    pass

class ArticleCategoryResponse(ArticleCategory):
    pass

# Схемы для запросов и ответов CRUD операций со статьей
class ArticleRequest(ArticleCreate):
    pass

class ArticleResponse(Article):
    pass
