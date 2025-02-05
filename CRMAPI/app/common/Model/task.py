from pydantic import BaseModel
from datetime import date
from typing import Optional


class TaskCreate(BaseModel):
    subject: str
    description: Optional[str] = None
    publishDate: str
    accountNumber: str
    clientName: str
    policyNumber: str
    status: str
    priority: str


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
