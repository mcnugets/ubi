from . import crud
from ..schema import user_schema
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional


def create_user(db: Session, user_create: user_schema.UserRequest):
    return crud.create_user(db=db, user_create=user_create)

def login_user(db: Session, login_user: user_schema.UserLogin):
    return crud.login(db=db, validate=login_user)

def get_user(db: Session, user_cred: Optional[Tuple[str, str]] = None):
