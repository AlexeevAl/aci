from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DATABASE_URL))
