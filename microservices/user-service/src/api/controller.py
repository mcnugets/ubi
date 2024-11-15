from . import crud
from ..schema import user_schema, token_schema
from fastapi import Depends, HTTPException, status
from typing import Annotated, Optional, Tuple, Dict
from ..security.authentication import decode_token
from sqlalchemy.orm import Session
from ..models import user
from ..security.authentication import authenticate, create_token, hash_pwd
import dotenv
from datetime import datetime, timedelta

# TODO: ADD ERRO HANDLING FOR EACH FUNCTION
def create_user(db: Session, user_create: user_schema.UserRequest) -> user.User:
     
    hashed_pwd = hash_pwd(user_create.password)
    return crud.create_user(db=db, user_create=user_create, hashed_password=hashed_pwd)

def login_user(db: Session, login_user: user_schema.UserLogin):
    return crud.login(db=db, validate=login_user)

def get_user(db: Session, user_cred: Optional[Tuple[str, str]] = None):
    return crud.get_user(db=db, user_cred=user_cred)


def get_authenticated_user(db:Session, pwd: str,  user_cred: Optional[Tuple[str, str]] = None) -> Optional[user.User]:
    
    user = get_user(db = db, user_cred=user_cred)
    if user is None:
        return False
    
    return user if authenticate(hashed_pwd=user.hashed_password, pwd=pwd) else None



# ====================
def create_access_token(dict:Optional[Dict[str, str]], algorithhm: str, expiry: timedelta) -> Optional[str]:
    
    token = create_token(dict=dict, algorithm=algorithhm, expiry=expiry)
    return token
    # dotenv.
    

    


def get_current_user(db:Session, payload: Annotated[str, Depends(decode_token)]):
    
    user_id: str = payload['id']

    token_data = token_schema.TokenPayload(user_id=user_id)
    
    user_data = get_user(db=db, user_cred=(token_data.user_id))

    return user_data
    # rest of the code
def get_current_active(current_user: Annotated[user_schema.UserRequest, None, Depends(get_current_user)]):
    
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Error: User is disabled")

    return current_user
    # the rest of the code


