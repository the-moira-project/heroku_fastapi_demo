from sqlmodel import create_engine
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE_URL = os.getenv('DB_URL')

engine = create_engine(DATABASE_URL, echo=True)
