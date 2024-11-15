from . import controller
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..models import user
from ..schema import user_schema, token_schema
from fastapi import Depends, HTTPException, status
from shared_database.connection import get_db
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
import dotenv
from datetime import datetime, timedelta, timezone
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

@router.post('/token')
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> token_schema.Token:

    auth_user = controller.get_authenticated_user(db=db, pwd=form_data.password, user_cred=(None, form_data.username))
    if auth_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error: Authentication failed", headers={"WWW-Authenticate": "Bearer"})
    if auth_user is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error: User not found")
    
    dic = {'username': auth_user.username}

    env = dotenv.dotenv_values()

    if env.get('ALGORITHM') is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Access token failed to create.")
    if env.get('EXPIRY') is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Token expiry value is missing.")
    access_token_expires = timedelta(minutes= int(env['EXPIRY']))
    
    access_token = controller.create_access_token(dict = dic, algorithhm=env['ALGORITHM'], expiry=access_token_expires)

    if access_token is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: access token is None')
    try:
        return token_schema.Token(access_token=access_token, token_type='bearer', expiry=str(access_token_expires))
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: {err}') from err