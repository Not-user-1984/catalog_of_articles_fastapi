from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (TIMESTAMP, Boolean, Column, DateTime, ForeignKey,
                        Integer, String,)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class ArticleCategory(Base):
    __tablename__ = "article_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    articles = relationship("Article", back_populates="category")

    def __str__(self):
        return str(self.name)


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime,
                        default=func.now(),
                        onupdate=func.now(),
                        nullable=False)
    category_id = Column(Integer,
                         ForeignKey("article_categories.id"),
                         nullable=False)
    category = relationship("ArticleCategory", back_populates="articles")
    authors = relationship("UserArticle", back_populates="article",
                           cascade="all, delete-orphan")


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    articles = relationship("UserArticle", back_populates="user")


class UserArticle(Base):
    __tablename__ = "user_article"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    user = relationship("User", back_populates="articles")
    article = relationship("Article", back_populates="authors")

    def __str__(self):
        return str(self.user_id)
