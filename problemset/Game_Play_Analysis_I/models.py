from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, Table

from utils.database import Base

metadata_obj = MetaData()

activity_table = Table(
    "activity",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("player_id", Integer),
    Column("device_id", Integer),
    Column("event_date", DateTime),
    Column("games_played", Integer),
)
