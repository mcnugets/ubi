from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR, Date
from sqlalchemy.orm import relationship
import os
# from .....shared_components.connection import base
from shared_database.connection import base

# user fields:
# user id
# user username
# user email address
# password (hashed)
# date
# name?


class User(base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    username = Column("username", String(100))
    email = Column("email", String(50))
    hashed_password = Column(String)
    date_login = Column("date login", Date)
    date_created = Column("date created", Date)
