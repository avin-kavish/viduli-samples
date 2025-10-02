from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select

from database import get_engine
from models import Article, ArticleCreate, ArticlePublic, ArticleUpdate


# Database functions
def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session


app = FastAPI(title="Articles API", description="A REST API for managing articles")


# CRUD endpoints for articles
@app.post("/articles/", response_model=ArticlePublic)
def create_article(article: ArticleCreate, session: Session = Depends(get_session)):
    """Create a new article"""
    db_article = Article.model_validate(article)
    session.add(db_article)
    session.commit()
    session.refresh(db_article)
    return db_article


@app.get("/articles/", response_model=List[ArticlePublic])
def read_articles(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    published: bool | None = None,
):
    """Read multiple articles with optional filtering"""
    query = select(Article)
    if published is not None:
        query = query.where(Article.published == published)
    articles = session.exec(query.offset(offset).limit(limit)).all()
    return articles


@app.get("/articles/{article_id}", response_model=ArticlePublic)
def read_article(article_id: int, session: Session = Depends(get_session)):
    """Read a single article by ID"""
    article = session.get(Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.patch("/articles/{article_id}", response_model=ArticlePublic)
def update_article(
    article_id: int, article: ArticleUpdate, session: Session = Depends(get_session)
):
    """Update an article"""
    article_db = session.get(Article, article_id)
    if not article_db:
        raise HTTPException(status_code=404, detail="Article not found")
    article_data = article.model_dump(exclude_unset=True)
    article_db.sqlmodel_update(article_data)
    session.add(article_db)
    session.commit()
    session.refresh(article_db)
    return article_db


@app.delete("/articles/{article_id}")
def delete_article(article_id: int, session: Session = Depends(get_session)):
    """Delete an article"""
    article = session.get(Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    session.delete(article)
    session.commit()
    return {"ok": True}


@app.get("/articles/hello-world")
async def hello_world():
    return {"message": "Hello World!"}
