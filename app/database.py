from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
import time


# SQLALCHEMY_DATABASE_URL = 'postgressql://postgres:Rajesh123@localhost/fastapi' # Dont know why this is not working 
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Rajesh123@localhost:5432/fastapi" # This link is working & do not use @ in the password 
# SQLALCHEMY_DATABASE_URL= mssql+pymssql://<username>:<password>@<host>:<port>/<database_name>/?charset=utf8 # sql connection string 
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"  # This is with env varible settings


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user = 'postgres',password = "Rajesh123",
#                                 cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection Scucessful')
#         break
#     except Exception as error:
#         print("Connecting to database failed ")
#         print("Error:", error)
#         time.sleep(5)

