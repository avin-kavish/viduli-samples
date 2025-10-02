from sqlmodel import Field, SQLModel


# Article models
class ArticleBase(SQLModel):
    title: str = Field(index=True)
    content: str
    author: str = Field(index=True)
    published: bool = Field(default=False)


class Article(ArticleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ArticlePublic(ArticleBase):
    id: int


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(SQLModel):
    title: str | None = None
    content: str | None = None
    author: str | None = None
    published: bool | None = None
