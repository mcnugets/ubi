from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# UserBase

# UserRequest
# UserResponse


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserRequest(UserBase):
    password: str
    date_created: datetime


class UserResponse(UserBase):
    id: int
    date_login: Optional[datetime]
    firstname: Optional[str]
    lastname: Optional[str]

    class Config:
        orm_mode = True

class UserLogin(UserBase): 
    password: str
    login_date: datetime

# for now we gonne leave it as it is but in the future I would need
# to create custom validator and additional code for annotations and further metadata development