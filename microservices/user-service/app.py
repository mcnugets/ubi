from fastapi import FastAPI, Depends
from .src.api.routes import router
from .dependencies import is_valid_token

from .src.models.user import base
from shared_database.connection import db_session, engine

# TODO: create generative token for authentication
# TODO: create proper sha256 hashing to hash password

base.metadata.create_all(bind=engine)
app = FastAPI()  # token param missing


app.include_router(router=router)


@app.get("/")
async def root():
    return {"message": "Can confirm this shit works"}
