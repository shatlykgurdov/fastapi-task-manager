from fastapi import FastAPI
from app.routes import auth_router, task_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}