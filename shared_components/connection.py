from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, URL, text
from configs import db_settngs
from sqlalchemy.orm import declarative_base


url_object = URL.create(
    drivername="postgresql",
    username=db_settngs.PGUSER,
    password=db_settngs.PGPASSWORD,
    host=db_settngs.PGHOST,
    database=db_settngs.PGDATABASE,
    port=db_settngs.PGPORT,
)
try:
    engine = create_engine(url_object)
    with engine.connect() as conn:
        conn.execute(text("select 1"))
        print(f"Connected to database: {db_settngs.PGUSER}")

    db_session = sessionmaker(bind=engine, autoflush=False)

except Exception as e:
    print(f"Error: {e}")

base = declarative_base()


# first we establish connection
# then we create models
# then we create schemas
# then we create routing
# then we create
