from sqlalchemy.orm import Session
from ..models import user
from ..schema import user_schema

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


def create_user(db: Session, user_create: user_schema.UserRequest):
    hashed_password = (
        user_create.password + "encrypted code"
    )  # requires sha-256 encryption
    try:
        db_user = user.User(
            email=user_create.email,
            username=user_create.username,
            date_created=user_create.date_created,
            hashed_password=hashed_password,
        )

        db.add(db_user)
        db.commit()
        print(f'The user has been successfully create: {user_create.username}')
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as sql_error:
        db.rollback()
        print(f"Error: {sql_error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {sql_error}",
        ) from sql_error


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr


# class UserRequest(UserBase):
#     password: str
#     date_created: datetime
