from datetime import date

from pydantic import BaseModel, Field


class FindSongResponse(BaseModel):
    id: int = Field(..., description="노래 ID", example="1")
    title: str = Field(..., description="노래 제목", example="촛불")
    artist: str = Field(..., description="노래 가수", example="조용필")
    base_date: date = Field(..., description="차트 기준일", example="1995-01-01")
    youtube_video_id: str = Field(
        ..., nullable=True, description="유튜브 비디오 ID", example="M7lc1UVf-VE"
    )
    music_chart_id: int = Field(..., description="뮤직 차트 ID", example="1")

    class Config:
        from_attributes = True
