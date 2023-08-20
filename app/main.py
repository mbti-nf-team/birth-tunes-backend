import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/music-charts/{music_chart_id}/song", response_model=schemas.FindSongResponse
)
def get_song(
    music_chart_id: int, birthdate: datetime.date, db: Session = Depends(get_db)
):
    db_song = crud.get_song_by_birthdate_and_music_chart(
        db=db,
        birthdate=birthdate,
        music_chart_id=music_chart_id,
    )
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
