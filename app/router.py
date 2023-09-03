import datetime

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get(
    "/music-charts/{music_chart_id}/song",
    description="뮤직 차트 ID랑 날짜로 노래 조회 (삭제 예정)",
    response_model=schemas.GetSongResponseDeprecated,
    deprecated=True,
)
def get_song_deprecated(
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


@router.get(
    "/songs/{year}/{month}/{day}",
    description="특정 날짜에 1위한 노래 조회",
    response_model=schemas.GetSongResponse,
)
def get_song(
    year: int = Path(..., ge=1981, le=2023, title="조회할 년도", example=1995),
    month: int = Path(..., ge=1, le=12, title="조회할 월", example=5),
    day: int = Path(..., ge=1, le=31, title="조회할 일", example=3),
    db: Session = Depends(get_db),
):
    db_song = crud.get_song_by_date(
        db=db,
        date=datetime.date(year, month, day),
    )
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
