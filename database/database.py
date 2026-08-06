
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from config import  DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


DATABASE_URL = (f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    
    
engine = create_engine(DATABASE_URL, echo=True)    


SessionLocal = sessionmaker( bind=engine, autoflush=False, autocommit=False,)


class Base(DeclarativeBase):
    pass

