import datetime

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get(
    "/music-charts/{music_chart_id}/song",
    description="날짜로 노래 조회",
    response_model=schemas.FindSongResponse,
)
def get_song(
    music_chart_id: int = Path(..., title="뮤직 차트 ID", example=1),
    date: datetime.date = Query(..., title="조회할 날짜", example="1995-05-03"),
    db: Session = Depends(get_db),
):
    db_song = crud.get_song_by_date_and_music_chart(
        db=db,
        date=date,
        music_chart_id=music_chart_id,
    )
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
