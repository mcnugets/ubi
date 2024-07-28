from . import controller
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..models import user
from ..schema import user_schema
from fastapi import Depends
from shared_database.connection import get_db


router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not found"}}
    )


# router = APIRouter(
#     prefix="/user",
#     tags=["user"],
#     responses={404: {"description": "not found"}}
# )
 
@router.post("/create_user")
def create_user(user: user_schema.UserRequest, db: Session = Depends(get_db)):
    return controller.create_user(db=db, user_create=user)

@router.post('/login')
def login_user():
    pass
