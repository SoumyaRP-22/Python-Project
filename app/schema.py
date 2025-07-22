from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class announcementCreate(BaseModel):
    title: str
    content: str

class announcementOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class LostFoundCreate(BaseModel):
    title: str
    description: str
    is_found: bool=False


class LostFoundOut(LostFoundCreate):
    id: int

    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
