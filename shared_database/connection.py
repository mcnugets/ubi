from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, URL, text
from configs import db_settngs
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Creating url objects using env vaeiables
url_object = URL.create(
    drivername="postgresql",
    username=db_settngs.PGUSER,
    password=db_settngs.PGPASSWORD,
    host=db_settngs.PGHOST,
    database=db_settngs.PGDATABASE,
    port=db_settngs.PGPORT,
)
# establishing connection
try:
    engine = create_engine(url_object)
    
    # add migration script
    # TODO: MODIFY THE MIGRATION SCRIPT TO MAKE MORE DYNAMIC AND REUSABLE
    with engine.connect() as conn:
        conn.execute(text("select 1"))
        print(f"Connected to database: {db_settngs.PGDATABASE}")

    db_session = sessionmaker(bind=engine, autoflush=False)
    
    # env.run_migrations_online_local([('ubi_db', engine)], db_session())

    def get_db():
        db = db_session()
        try:
            yield db
        except SQLAlchemyError as err:
            print(f"Error: {err}")

        finally:
            db.close()

except Exception as e:
    print(f"Error: {e}")

# returning the base to inherit for data model creation
base = declarative_base()

