from sqlmodel import Session
from db import engine
from models import *


# scratch pad for functions to export to other files

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def add_snapshot(data: Snapshot):
    with Session(engine) as session:
        session.add(data)

        session.commit()

    return {"message": "Snapshot added"}


def view_last_ten_snapshots():
    with Session(engine) as session:
        snapshots = session.query(Snapshot).order_by(Snapshot.time.desc()).limit(10).all()

        for snapshot in snapshots:
            print(snapshot)

        return snapshots
