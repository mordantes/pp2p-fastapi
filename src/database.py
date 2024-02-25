from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_PWD, DB_USER, DB_HOST,DB_NAME


# sqlite_engine = create_engine("sqlite:///prods.sqlite3")

sqlite_engine = create_engine(
    "sqlite:////Users/ivan322/Projects/PP2P/parser/prods.sqlite3"
)
engine_msql = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4")



Base = declarative_base()
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine_msql)


def get_session():
    with session_maker() as session:
        yield session


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
