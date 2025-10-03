import os
from sqlmodel import SQLModel, create_engine
import redis

# Import models to ensure they're registered with SQLModel metadata
from models import Article

# Database configuration
DATABASE_URL = os.getenv(
    "ARTICLES_DB_URL", "postgresql://username:password@localhost/articles_db"
)

# Redis configuration for tags store
TAGS_STORE_URL = os.getenv(
    "TAGS_STORE_URL", "redis://localhost:6379"
)

# SQLAlchemy will automatically use psycopg3 if available
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# Redis client for tags store
redis_client = redis.from_url(TAGS_STORE_URL)


def create_db_and_tables():
    """Create all database tables defined in SQLModel models."""
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully!")


def get_engine():
    """Get the database engine instance."""
    return engine


def get_redis_client():
    """Get the redis client instance."""
    return redis_client
