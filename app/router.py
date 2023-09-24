import datetime

from fastapi import APIRouter, Depends, HTTPException, Path, Request
from sqlalchemy.orm import Session

from . import crud, schemas
from .auth import get_api_key
from .database import get_db

router = APIRouter()


@router.get(
    "/songs/{year}/{month}/{day}",
    description="특정 날짜에 1위한 노래 조회",
    response_model=schemas.GetSongResponse,
)
def get_song(
    request: Request,
    year: int = Path(..., ge=1981, le=2023, title="조회할 년도", example=1995),
    month: int = Path(..., ge=1, le=12, title="조회할 월", example=5),
    day: int = Path(..., ge=1, le=31, title="조회할 일", example=3),
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key),
):
    db_song = crud.get_song_by_date(
        db=db,
        date=datetime.date(year, month, day),
    )
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
