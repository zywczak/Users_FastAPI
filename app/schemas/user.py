from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    name: constr(min_length=3)
    email: EmailStr

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    total: int
    users: list[UserResponse]
