from pydantic import BaseModel
from typing import List, Optional


class Job(BaseModel):
    name: str
    status: str
    timestamp: Optional[str] = None


class Pipeline(BaseModel):
    name: str
    jobs: List[Job]
    status: str
