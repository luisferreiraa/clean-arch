# presentation/schemas/user.py
from typing import Optional, List

from pydantic import BaseModel, EmailStr

from clean_arch.presentation.schemas.post import PostResponse


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    disabled: bool | None = None


class UserResponse(UserBase):
    id: int
    disabled: bool
    posts: Optional[List[PostResponse]] = []


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None


class Config:
    orm_mode = True
