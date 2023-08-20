from datetime import date

from pydantic import BaseModel


class FindSongResponse(BaseModel):
    id: int
    title: str
    artist: str
    base_date: date
    youtube_video_id: str
    music_chart_id: int

    class Config:
        from_attributes = True
