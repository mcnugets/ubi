from fastapi import FastAPI, Depends
from .src.api.routes import router
from .dependencies import is_valid_token

# TODO: create generative token for authentication
# TODO: create proper sha256 hashing to hash password
app = FastAPI()  # token param missing


app.include_router(router=router)
