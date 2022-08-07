from sqlmodel import create_engine
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

engine = create_engine(conn, echo=True)
