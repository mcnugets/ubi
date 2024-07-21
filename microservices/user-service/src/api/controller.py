from . import crud
from ..schema import user_schema
from fastapi import Depends
from sqlalchemy.orm import Session


def create_user(db: Session, user_create: user_schema.UserRequest):
    return crud.create_user(db=db, user_create=user_create)
