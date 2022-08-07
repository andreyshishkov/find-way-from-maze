from pydantic import BaseModel
from typing import Dict, List


class Request(BaseModel):
    graph: Dict[str, List[str]]
    start: str
    finish: str


class Response(BaseModel):
    num: int
    path: str