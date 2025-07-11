from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.db.session import AsyncSessionLocal
from app.db import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)
from app.schemas import TaskCreate, TaskUpdate, TaskOut
from app.models.user import User
from app.routes.auth import get_current_user

router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/tasks/", response_model=TaskOut)
async def create_new_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await create_task(db, task, owner_id=current_user.id)


@router.get("/tasks/", response_model=List[TaskOut])
async def list_tasks(
    status: Optional[bool] = None,
    sort: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await get_tasks(
        db,
        owner_id=current_user.id,
        status=status,
        sort_by_priority=(sort == "priority"),
    )


@router.get("/tasks/{task_id}", response_model=TaskOut)
async def retrieve_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskOut)
async def update_existing_task(
    task_id: int,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = await update_task(db, task_id, current_user.id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}")
async def delete_existing_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    success = await delete_task(db, task_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
