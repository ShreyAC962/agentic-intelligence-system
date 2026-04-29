# To establish connection to database and communicates with PostgreSQL
from sqlalchemy import create_engine
# To cretae database sessions - Is used to interact with the database(run queries, insert data, etc)
from sqlalchemy.orm import sessionmaker
from app.config import DB_URL

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine)