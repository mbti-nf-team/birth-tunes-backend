import datetime

from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models


def get_song_by_date_and_music_chart(
    db: Session, date: datetime.date, music_chart_id: int
):
    return (
        db.query(models.Song)
        .filter(models.Song.music_chart_id == music_chart_id)
        .filter(models.Song.base_date <= date)
        .order_by(desc(models.Song.base_date))
        .first()
    )
