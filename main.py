from sqlmodel import Session
from db import engine
from fastapi import FastAPI
from models import Snapshot


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/snapshot")
async def add_snapshot(snapshot: Snapshot):
    with Session(engine) as session:
        session.add(snapshot)

        session.commit()

    return {"message": "Snapshot added"}


@app.get("/recent_snapshots")
async def view_recent_snapshots():
    with Session(engine) as session:
        snapshots = session.query(Snapshot).order_by(Snapshot.time.desc()).limit(10).all()

        for snapshot in snapshots:
            print(snapshot)

        return snapshots
