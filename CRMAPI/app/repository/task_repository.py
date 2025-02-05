from aiocache import Cache
from app.common.Model.task import TaskCreate, Task
from typing import List
import json

# Cache configuration
cache = Cache(Cache.MEMORY)
CACHE_KEY = "tasks"


class TaskRepository:
    async def load_tasks_to_cache(self) -> None:
        """Load tasks from tasks.json into cache on application startup."""
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)
        tasks = [Task(**task) for task in tasks_data]
        await cache.set(CACHE_KEY, tasks)

    async def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from the cache."""
        tasks = await cache.get(CACHE_KEY)
        if tasks is None:
            # If cache is empty, initialize it
            await self.load_tasks_to_cache()
            tasks = await cache.get(CACHE_KEY)
        return tasks

    async def create_task(self, task: TaskCreate) -> Task:
        """Add a new task to the cache."""
        tasks = await self.get_all_tasks()
        new_id = len(tasks) + 1  # Generate a new task ID
        new_task = Task(id=new_id, **task.dict())

        # Add the new task and update cache
        tasks.append(new_task)
        await cache.set(CACHE_KEY, tasks)
        return new_task
