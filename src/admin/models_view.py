from sqladmin import ModelView
from db.models import Article, ArticleCategory, User


class ArticleAdmin(ModelView, model=Article):
    column_list = [
        Article.id,
        Article.title,
        Article.created_at
    ]
    column_searchable_list = [Article.id, Article.title]
    column_sortable_list = [Article.id]


class ArticleCategoryAdmin(ModelView, model=ArticleCategory):
    column_list = [
        ArticleCategory.id,
        ArticleCategory.name,

    ]
    column_searchable_list = [ArticleCategory.id, ArticleCategory.name]
    column_sortable_list = [Article.id]


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.email,

    ]
    column_searchable_list = [User.id, User.email]
    column_sortable_list = [Article.id]
