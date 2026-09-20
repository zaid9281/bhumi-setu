from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.CLERK
    district: str | None = None


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: UserRole
    district: str | None

    class Config:
        from_attributes = True
