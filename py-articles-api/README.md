# FastAPI Articles CRUD API

A REST API for managing articles built with FastAPI and SQLModel, using PostgreSQL as the database.

## Features

- **CRUD Operations**: Create, Read, Update, Delete articles
- **Filtering**: Filter articles by published status
- **Pagination**: Support for offset and limit parameters
- **Auto-generated Documentation**: Interactive API docs with Swagger UI and ReDoc
- **PostgreSQL Integration**: Uses SQLModel for ORM and data modeling

## Article Model

Each article has the following fields:

- `id`: Unique identifier (auto-generated)
- `title`: Article title (required, indexed)
- `content`: Article content (required)
- `author`: Article author (required, indexed)
- `published`: Publication status (boolean, defaults to false)

## API Endpoints

### Articles

- `POST /articles/` - Create a new article
- `GET /articles/` - List all articles (with optional filtering and pagination)
- `GET /articles/{article_id}` - Get a specific article by ID
- `PATCH /articles/{article_id}` - Update an article
- `DELETE /articles/{article_id}` - Delete an article

### Test

- `GET /hello-world` - Simple hello world endpoint

## Setup

1. **Install Poetry** (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Install dependencies**:

```bash
poetry install
```

3. **Set up PostgreSQL database**:

   - Create a PostgreSQL database named `articles_db`
   - Set the `ARTICLES_DB_URL` environment variable with your database credentials:

   ```bash
   export ARTICLES_DB_URL="postgresql://username:password@localhost/articles_db"
   ```

4. **Create database tables**:

   ```bash
   python manage.py create_db
   ```

## Running the Application

Start the server with:

```bash
poetry run fastapi dev
```

The application will be available at http://localhost:8000

## Management Commands

The application includes management commands for database operations:

```bash
# Create database tables
python manage.py create_db

# Show help
python manage.py --help
```

## API Documentation

Access the automatic API documentation at:

- **Swagger UI**: http://localhost:8000/docs

## Example API Usage

### Create an Article

```bash
curl -X POST "http://localhost:8000/articles/" \
-H "Content-Type: application/json" \
-d '{
  "title": "My First Article",
  "content": "This is the content of my article.",
  "author": "John Doe",
  "published": true
}'
```

### List Articles

```bash
curl "http://localhost:8000/articles/"
```

### Get a Specific Article

```bash
curl "http://localhost:8000/articles/1"
```

### Update an Article

```bash
curl -X PATCH "http://localhost:8000/articles/1" \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Title",
  "published": true
}'
```

### Delete an Article

```bash
curl -X DELETE "http://localhost:8000/articles/1"
```
