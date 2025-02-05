import json
from app.repository.task_repository import TaskRepository
from app.common.Model.task import TaskCreate, Task
from typing import List


class TaskService:
    async def list_tasks(self):
        task_repository = TaskRepository()
        return await task_repository.get_all_tasks()

    async def add_task(self,task: TaskCreate):
        task_repository = TaskRepository()
        return await task_repository.create_task(task)

