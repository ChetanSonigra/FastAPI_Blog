from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog_api.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

session_local = Session(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()