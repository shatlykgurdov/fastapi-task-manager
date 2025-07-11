from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from typing import List, Optional


async def create_task(db: AsyncSession, task: TaskCreate, owner_id: int) -> Task:
    db_task = Task(**task.dict(), owner_id=owner_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def get_tasks(
    db: AsyncSession,
    owner_id: int,
    status: Optional[bool] = None,
    sort_by_priority: bool = False
) -> List[Task]:
    stmt = select(Task).where(Task.owner_id == owner_id)
    if status is not None:
        stmt = stmt.where(Task.is_completed == status)
    if sort_by_priority:
        stmt = stmt.order_by(Task.priority.desc())
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_task(db: AsyncSession, task_id: int, owner_id: int) -> Optional[Task]:
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.owner_id == owner_id)
    )
    return result.scalar_one_or_none()


async def update_task(db: AsyncSession, task_id: int, owner_id: int, task_data: TaskUpdate) -> Optional[Task]:
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.owner_id == owner_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        return None
    for field, value in task_data.dict(exclude_unset=True).items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int, owner_id: int) -> bool:
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.owner_id == owner_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True
