from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: UUID
    is_active: bool
    role: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
