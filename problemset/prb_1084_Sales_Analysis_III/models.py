import datetime

from sqlalchemy import (VARCHAR, Column, Date, ForeignKey, Integer, MetaData,
                        Table)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import PRIMARY_KEY, Base


class ProductOrm(Base):
    __tablename__ = "product"
    product_id: Mapped[PRIMARY_KEY]
    product_name: Mapped[str] = mapped_column(VARCHAR(10))
    unit_price: Mapped[int]

    sales: Mapped[list["SalesOrm"]] = relationship(
        back_populates="product"
    )


class SalesOrm(Base):
    __tablename__ = "sales"
    id: Mapped[PRIMARY_KEY]
    seller_id: Mapped[int]
    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.product_id", ondelete="CASCADE")
    )
    buyer_id: Mapped[int]
    sale_date: Mapped[datetime.date]
    quantity: Mapped[int]
    price: Mapped[int]

    product: Mapped["ProductOrm"] = relationship(
        back_populates="sales"
    )


metadata_obj = MetaData()

product_table = Table(
    "product",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", VARCHAR(10)),
    Column("unit_price", Integer)
)

sales_table = Table(
    "sales",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("seller_id", Integer),
    Column(
        "product_id",
        Integer,
        ForeignKey("product.product_id", ondelete="CASCADE")
    ),
    Column("buyer_id", Integer),
    Column("sale_date", Date),
    Column("quantity", Integer),
    Column("price", Integer)
)
