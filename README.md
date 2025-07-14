# 📝 FastAPI Task Manager

A simple Task Management System built with **FastAPI**, **Async SQLAlchemy**, **Alembic**, **PostgreSQL**, and **JWT Authentication**. It allows users to register, log in, and manage tasks.

---

## 🚀 Features

- 🔐 JWT-based user authentication (register/login)
- ✅ Task CRUD with authentication
- 🛠️ PostgreSQL database (async via SQLAlchemy)
- 📦 Alembic for database migrations
- 🐳 Docker and Docker Compose support
- 🧪 Pytest setup for API testing

---

### 🧱 Tech Stack

* **Python 3.12** – Latest stable version with improved typing and performance
* **FastAPI** – Modern, fast web framework for building APIs with Python 3.6+
* **SQLAlchemy (async)** – Async ORM for database interaction
* **Pydantic** – Data validation and parsing using Python type annotations
* **Alembic** – Database migration tool for SQLAlchemy
* **PostgreSQL** – Relational database for storing tasks and users
* **Docker & Docker Compose** – For containerized deployment
* **Pytest + HTTPX** – For automated API testing
* **Poetry** – Tool for dependency management and packaging

---

### 📁 Project Structure

```bash
.
├── app/
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic models for validation and serialization
│   ├── routes/           # Route handlers
│   ├── database.py       # Database session and engine setup
│   └── main.py           # FastAPI app initialization
├── alembic/              # Database migrations
├── docker-compose.yml    # Docker orchestration
├── Dockerfile            # Docker container definition
├── .env.example          # Environment variable template
├── README.md
└── pyproject.toml        # Poetry configuration
````

---

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Poetry (`pip install poetry`)

---

### 🧪 Local Development (without Docker)

Create a `.env` file in the root directory with the following content:

```env
# Database connection URL (adjust username, password, host, and DB name as needed)
DATABASE_URL=postgresql+asyncpg://your_username:your_password@your_host:5432/your_database

# JWT secret key (replace with a secure random string)
SECRET_KEY=your_secret_key
````

You can generate a secure secret key with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Then run:

```bash
# Install dependencies
poetry install

# Activate virtualenv
poetry shell  # or poetry env activate <env_path>

# Run migrations
alembic upgrade head

# Run server
uvicorn app.main:app --reload --port 8001
```

---

### 🐳 Run with Docker

Create a `.env` file in the project root with the following content:

```env
DATABASE_URL=postgresql+asyncpg://your_username:your_password@db:5432/your_database
SECRET_KEY=your_secret_key
```

Ensure `start.sh` uses **Unix-style (LF)** line endings. If you're on Windows and encounter:

```
$'\r': command not found
```

Fix it in **VS Code**:

* Open `start.sh`
* Click `CRLF` in the bottom-right
* Select `LF`
* Save the file

Generate a secure secret key with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Then build and run:

```bash
docker-compose up --build
```

Docker will:

* Set up the PostgreSQL database
* Apply Alembic migrations
* Run the FastAPI app

Access the app at: [http://localhost:8001](http://localhost:8001)

---

## 🔐 API Endpoints

| Method | Endpoint         | Description         | Auth Required |
| ------ | ---------------- | ------------------- | ------------- |
| POST   | `/auth/register` | Register a new user | ❌             |
| POST   | `/auth/login`    | Login and get token | ❌             |
| GET    | `/auth/me`       | Get current user    | ✅             |
| CRUD   | `/tasks`         | Manage tasks        | ✅             |
| GET    | `/`              | Root endpoint       | ❌             |

Use the JWT token from login in the `Authorization: Bearer <token>` header.

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📘 API Docs

* Swagger UI: [http://localhost:8001/docs](http://localhost:8001/docs)
* Redoc: [http://localhost:8001/redoc](http://localhost:8001/redoc)

---

## 📄 License

MIT License – use freely and modify as needed.