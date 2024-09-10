from pydantic import BaseModel
from typing import Annotated, Union


class Token(BaseModel):
    access_token: str
    token_type: str
    expiry:str

class TokenPayload(BaseModel):
    user_id: Union[None, str] = None
    
