from pydantic import BaseModel
from typing import Optional

class TaskResponse(BaseModel):
    task_id: str

class TaskStatusResponse(BaseModel):
    status: str
    result: Optional[str]
