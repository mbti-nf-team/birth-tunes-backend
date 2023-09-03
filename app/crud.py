import datetime

from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models


def get_song_by_date(db: Session, date: datetime.date):
    return (
        db.query(models.Song)
        .filter(models.Song.base_date <= date)
        .order_by(desc(models.Song.base_date))
        .first()
    )
