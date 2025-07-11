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

## 🧱 Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Alembic
- Docker
- Pytest
- Poetry

---

## 📂 Project Structure

```

fastapi\_task\_manager/
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── db/
│   ├── core/
├── alembic/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md

````

---

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Poetry (`pip install poetry`)

---

### 🧪 Local Development (without Docker)

# .env 
Your project requires a .env file in the root directory. Here's how it should look:
#Database connection URL (adjust username, password, host, and DB name as needed)
#JWT secret key (replace with a secure random string)

DATABASE_URL=postgresql+asyncpg://your_username:your_password@your_host:5432/your_database
SECRET_KEY=your_secret_key

You can generate a secure secret key with:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"


```bash
# Install dependencies
poetry install

# Activate virtualenv
poetry env activate <env_path>  # or use `poetry shell`

# Run migrations
alembic upgrade head


# Run server
uvicorn app.main:app --reload --port 8001
````

---

### 🐳 Run with Docker

Create a .env file in the project root with the following content:

DATABASE_URL=postgresql+asyncpg://your_user_name:your_passwor@db:5432/task_db
SECRET_KEY=your_secret_key

Make sure start.sh uses Unix-style (LF) line endings. If you're on Windows and encounter:
$'\r': command not found

Fix it by:
In VSCode:
Open start.sh
Click CRLF in the bottom-right
Select LF
Save the file


You can generate a secure secret key with:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"



```bash
# Build and run the containers
docker-compose up --build
```

Docker will:

* Set up the PostgreSQL database
* Apply Alembic migrations
* Run the FastAPI app

Access it at: [http://localhost:8001](http://localhost:8001)

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

