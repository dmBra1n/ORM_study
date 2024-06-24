import datetime

from sqlalchemy import (VARCHAR, Column, Date, ForeignKey, Integer, MetaData,
                        Table)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import PRIMARY_KEY, Base


class SalesPersonModel(Base):
    __tablename__ = "salesperson"
    sales_id: Mapped[PRIMARY_KEY]
    name: Mapped[str] = mapped_column(VARCHAR(255))
    salary: Mapped[int]
    commission_rate: Mapped[int]
    hire_date: Mapped[datetime.date]

    orders: Mapped[list["OrdersModel"]] = relationship(
        back_populates="salesperson"
    )


class CompanyModel(Base):
    __tablename__ = "company"
    com_id: Mapped[PRIMARY_KEY]
    name: Mapped[str] = mapped_column(VARCHAR(255))
    city: Mapped[str] = mapped_column(VARCHAR(255))

    orders: Mapped[list["OrdersModel"]] = relationship(
        back_populates="company"
    )


class OrdersModel(Base):
    __tablename__ = "orders"
    order_id: Mapped[PRIMARY_KEY]
    order_date: Mapped[datetime.date]
    com_id: Mapped[int] = mapped_column(
        ForeignKey("company.com_id", ondelete="CASCADE")
    )
    sales_id: Mapped[int] = mapped_column(
        ForeignKey("salesperson.sales_id", ondelete="CASCADE")
    )
    amount: Mapped[int]

    salesperson: Mapped["SalesPersonModel"] = relationship(
        back_populates="orders"
    )
    company: Mapped["CompanyModel"] = relationship(
        back_populates="orders"
    )


metadata_obj = MetaData()

sales_person_table = Table(
    "salesperson",
    metadata_obj,
    Column("sales_id", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(255)),
    Column("salary", Integer),
    Column("commission_rate", Integer),
    Column("hire_date", Date),
)

company_table = Table(
    "company",
    metadata_obj,
    Column("com_id", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(255)),
    Column("city", VARCHAR(255)),
)

orders_table = Table(
    "orders",
    metadata_obj,
    Column("order_id", Integer, primary_key=True, autoincrement=True),
    Column("order_date", Date),
    Column(
        "com_id",
        Integer,
        ForeignKey("company.com_id", ondelete="CASCADE")
    ),
    Column(
        "sales_id",
        Integer,
        ForeignKey("salesperson.sales_id", ondelete="CASCADE")
    ),
    Column("amount", Integer),
)
