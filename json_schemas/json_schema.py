from typing import Dict, List, Any
from pydantic import BaseModel


class Meme(BaseModel):
    id: int
    info: Dict[str, Any]
    tags: List[str]
    text: str
    updated_by: str
    url: str


class Data(BaseModel):
    data: List[Meme]
