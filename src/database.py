from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_engine = create_engine("sqlite:///prods.sqlite3")

Base = declarative_base()
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sqlite_engine)



def get_session():
    with session_maker() as session:
        yield session


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
