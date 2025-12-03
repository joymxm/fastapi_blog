from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=4, max_length=200, description="User password")

class ShowUser(BaseModel):
    email: EmailStr 
    is_active: bool

    class Config:
        from_attributes = True


