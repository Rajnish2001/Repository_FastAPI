from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' #Connect to the database

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}) #create engine

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False) #Create SessionLocal

Base = declarative_base()

#Create database instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close_all() 
    