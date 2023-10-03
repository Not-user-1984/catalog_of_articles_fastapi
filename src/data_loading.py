from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from db.models import User, ArticleCategory, Article, UserArticle
import random


fake = Faker()


def create_users(session):
    users = []
    for _ in range(30):
        user = User(
            email=fake.email(),
            username=fake.user_name(),
            registered_at=fake.date_time_this_decade(),
            hashed_password="your_password_hash_here",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        users.append(user)
    session.add_all(users)
    session.commit()


def create_categories(session):
    categories = []
    for i in range(25):
        category = ArticleCategory(
            name=fake.word() + str(i),
        )
        categories.append(category)

    session.add_all(categories)
    session.commit()


def create_articles(session, users, categories):
    for i in range(250):
        user = random.choice(users)
        category = random.choice(categories)
        article = Article(
            title=fake.sentence() + str(i),
            description=fake.paragraph() + str(i),
            link=fake.url(),
            created_at=fake.date_time_this_decade(),
            updated_at=fake.date_time_this_decade(),
            category=category,
            authors=[UserArticle(user=user)],
        )

        try:
            session.add(article)
            session.commit()
        except IntegrityError:
            session.rollback()


if __name__ == "__main__":
    from config import settings
    engine = create_engine(settings.DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    create_users(session)
    create_categories(session)
    users = session.query(User).all()
    categories = session.query(ArticleCategory).all()
    create_articles(session, users, categories)
