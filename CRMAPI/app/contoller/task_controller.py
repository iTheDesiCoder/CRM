from fastapi import APIRouter, Depends
from app.manager.task_service import TaskService
from app.common.Model.task import TaskCreate, Task

router = APIRouter()


class TasksController:
    @router.get("/tasks", response_model=list[Task])
    async def get_tasks():
        task_service = TaskService()
        return await task_service.list_tasks()

    @router.post("/tasks", response_model=Task)
    async def create_new_task(task: TaskCreate):
        task_service = TaskService()
        return await task_service.add_task(task)
