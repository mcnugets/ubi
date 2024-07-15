from typing import Annotated
from fastapi import Header, HTTPException


def is_valid_token(x_token: Annotated[str, Header()]):
    if x_token != '1234': # this needs to be changed later
        raise HTTPException(status_code=400, detail='Invalid X-Tolken')
    