import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
#创建base
Base = declarative_base()

MYSQL_URL = os.getenv("MYSQL_URL")
#创建engine
engine = create_engine(MYSQL_URL)
#创建session
SessionLocal = sessionmaker(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()