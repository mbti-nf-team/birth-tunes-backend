from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class MusicChart(BaseModel):
    id: int = Field(..., description="뮤직 차트 ID", example="1")
    name: str = Field(..., description="뮤직 차트 이름", example="가요톱10")

    class Config:
        from_attributes = True


class Song(BaseModel):
    id: int = Field(..., description="노래 ID", example="1")
    title: str = Field(..., description="노래 제목", example="촛불")
    artist: str = Field(..., description="노래 가수", example="조용필")
    base_date: date = Field(..., description="차트 기준일", example="1995-01-01")
    youtube_video_id: Optional[str] = Field(
        ..., description="유튜브 비디오 ID", example="M7lc1UVf-VE"
    )

    class Config:
        from_attributes = True


class GetSongResponse(Song):
    music_chart: MusicChart = Field(..., description="뮤직 차트 정보")
