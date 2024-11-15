from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..models import user
from ..schema import user_schema
from typing import Tuple, Optional
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from fastapi import HTTPException, status


# end of the section
def create_user(db: Session, user_create: user_schema.UserRequest, hashed_password: str ):
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


def get_user(db: Session, user_cred: Optional[Tuple[Optional[str], Optional[str]]] = (None, None)):
    """
    Organizes a list of integers into a tuple of two lists:
    - The first list contains all the 1s.
    - The second list contains all the 2s.
    
    Parameters:
    data (list): A list of integers to be organized.

    Returns:
    Tuple[list, list]: A tuple containing two lists (1s and 2s).
    """
    (email, username) = user_cred
   
    try:
        return db.query(user.User).filter(or_(user.User.email == email, user.User.username == username)).first()
    except NoResultFound as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Error: {err}')





# Example code
# def get_user_by_email(db: Session, email: str):
    # return db.query(models.User).filter(models.User.email == email).first()
