# presentation/schemas/post.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    author: int
    date: datetime


class PostResponse(PostBase):
    id: int


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class Config:
    orm_mode = True
