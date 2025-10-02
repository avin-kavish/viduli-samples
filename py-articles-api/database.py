import os
from sqlmodel import SQLModel, create_engine

# Import models to ensure they're registered with SQLModel metadata
from models import Article

# Database configuration
DATABASE_URL = os.getenv(
    "ARTICLES_DB_URL", "postgresql://username:password@localhost/articles_db"
)
# SQLAlchemy will automatically use psycopg3 if available
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    """Create all database tables defined in SQLModel models."""
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully!")


def get_engine():
    """Get the database engine instance."""
    return engine
