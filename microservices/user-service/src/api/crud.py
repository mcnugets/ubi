from sqlalchemy.orm import Session
from ..models import user
from ..schema import user_schema
from typing import Tuple, Optional
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from fastapi import HTTPException, status

# cryptography and authorization section
import secrets
from argon2 import PasswordHasher
# end of the section
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


def get_user(db: Session, user_cred: Optional[Tuple[str, str]] = None):
    (email, username) = user_cred
   
    try:
        return db.query(user.User).filter(user.User.email == email or user.User.username == username).first()
    
    except NoResultFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Error: {err}')



 
def login_user(db: Session, user_login: user_schema.UserLogin):
    try:
        user_cred = (user_login.username, user_login.email)
        find_user = get_user(db=db, user_cred=user_cred)
        if find_user:
            
            
        

            # this section goes to security directory
            # salt = secrets.token_bytes(16)

            db_hash_salt = find_user.hashed_password.split(':')
            input_salted_pass = db_hash_salt[0] + user_login.password 

            ph = PasswordHasher()

            hashed_input_p = ph.hash(input_salted_pass)

            

            if ph.verify(db_hash_salt[1], hashed_input_p):
                
                # 1. convert to json
                # 2. put find_user to json
                # 3. generate token
                # 4. put token to json
                # 5. return the variable
                pass
                # and then we return a user template in json/xml or whatever form
                # we also generate token for cookie/session adn then return that also
                # we return user info
            


    except ValueError as err:

# Example code
# def get_user_by_email(db: Session, email: str):
    # return db.query(models.User).filter(models.User.email == email).first()
