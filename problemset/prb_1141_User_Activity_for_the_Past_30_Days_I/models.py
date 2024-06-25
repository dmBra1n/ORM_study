import datetime
import enum

from sqlalchemy import Column, Date, Enum, Integer, MetaData, Table
from sqlalchemy.orm import Mapped

from utils.database import PRIMARY_KEY, Base


class ActivityType(enum.Enum):
    open_session = 'open_session'
    end_session = "end_session"
    scroll_down = "scroll_down"
    send_message = "send_message"


class ActivityOrm(Base):
    __tablename__ = "activity"
    id: Mapped[PRIMARY_KEY]
    user_id: Mapped[int]
    session_id: Mapped[int]
    activity_date: Mapped[datetime.date]
    activity_type: Mapped[ActivityType]


metadata_obj = MetaData()

activity_table = Table(
    "activity",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer),
    Column("session_id", Integer),
    Column("activity_date", Date),
    Column("activity_type", Enum(ActivityType))
)
