"""create models

Revision ID: 9139609ae382
Revises: 
Create Date: 2023-08-19 23:32:11.946030

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9139609ae382"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "music_chart",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_music_chart_id"), "music_chart", ["id"], unique=False)
    op.create_table(
        "song",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("artist", sa.String(length=100), nullable=False),
        sa.Column("base_date", sa.Date(), nullable=False),
        sa.Column("content_url", sa.String(), nullable=True),
        sa.Column("music_chart_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["music_chart_id"],
            ["music_chart.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("base_date", "music_chart_id"),
    )
    op.create_index(op.f("ix_song_id"), "song", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_song_id"), table_name="song")
    op.drop_table("song")
    op.drop_index(op.f("ix_music_chart_id"), table_name="music_chart")
    op.drop_table("music_chart")
    # ### end Alembic commands ###