from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import relationship

from .database import Base


class MusicChart(Base):
    __tablename__ = "music_chart"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    songs = relationship("Song", back_populates="music_chart")


class Song(Base):
    __tablename__ = "song"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    artist = Column(String(100), nullable=False)
    base_date = Column(Date, nullable=False, index=True)
    youtube_video_id = Column(String(100), nullable=True)
    music_chart_id = Column(Integer, ForeignKey("music_chart.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    music_chart = relationship("MusicChart", back_populates="songs")

    __table_args__ = (UniqueConstraint("base_date", "music_chart_id"),)
