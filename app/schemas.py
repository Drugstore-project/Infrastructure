"""
Schemas for Auth Service.
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    cpf: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: constr(min_length=6)
    role_id: int

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    cpf: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    is_active: bool
    role_id: int

    class Config:
        from_attributes = True

class LoginInput(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
