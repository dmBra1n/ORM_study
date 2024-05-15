from typing import Annotated

from sqlalchemy import Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class FollowersOrm(Base):
    __tablename__ = "followers"
    id: Mapped[intpk]
    user_id: Mapped[int]
    follower_id: Mapped[int]


metadata_obj = MetaData()

followers_table = Table(
    'followers',
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("follower_id", Integer)
)
