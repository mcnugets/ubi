from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, URL
from configs import db_settngs
from sqlalchemy.ext.declarative import declarative_base


url_object = URL.create(
    drivername="postgresql",
    username=db_settngs.PGHOST,
    password=db_settngs.PGPASSWORD,
    host=db_settngs.PGHOST,
    database=db_settngs.PGDATABASE,
    port=db_settngs.PGPORT,
)

engine = create_engine(url_object)
db_session = sessionmaker(bind=engine, autoflush=False)

base = declarative_base()
