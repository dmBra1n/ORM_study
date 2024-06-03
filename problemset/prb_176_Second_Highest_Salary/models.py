from sqlalchemy import Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped

from utils.database import PRIMARY_KEY, Base


class EmployeeOrm(Base):
    __tablename__ = "employee"
    id: Mapped[PRIMARY_KEY]
    salary: Mapped[int]


metadata_obj = MetaData()

employee_table = Table(
    "employee",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("salary", Integer)
)
