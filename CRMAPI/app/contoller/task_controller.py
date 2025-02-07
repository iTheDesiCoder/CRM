from fastapi import APIRouter, HTTPException
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

    @router.post("/vendor/alerts", response_model=Task)
    async def create_task_from_vendor(alert_payload: dict):
        """Create a task from an incoming vendor alert payload."""
        try:
            task_service = TaskService()
            task = await task_service.convert_and_save_task(alert_payload)
            return task
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.put("/tasks/{task_id}", response_model=Task)
    async def update_task(task_id: int, updated_task: TaskCreate):
        try:
            # Update the task in memory cache using the service layer
            task_service = TaskService()
            task = await task_service.update_task_in_cache(task_id, updated_task)
            if task is None:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/tasks/{task_id}", response_model=Task)
    async def get_task(task_id: int):
        task_service = TaskService()
        tasks = await task_service.list_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        raise HTTPException(status_code=404, detail="Task not found")