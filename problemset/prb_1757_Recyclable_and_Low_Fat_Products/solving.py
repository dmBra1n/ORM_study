from models import ProductsOrm
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class RecyclableAndLowFatProductsCore(BaseCore):
    def find_products(self):
        with self.session() as session:
            query = (
                """SELECT product_id
                    FROM Products
                    WHERE low_fats = 'Y' AND recyclable = 'Y';"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class RecyclableAndLowFatProductsCoreOrm(BaseOrm):
    def find_products(self):
        products = aliased(ProductsOrm)
        try:
            with self.session() as session:
                query = (
                    select(products.product_id)
                    .where(
                        products.low_fats == "Y",
                        products.recyclable == "Y"
                    )
                )
                result = session.execute(query)
                DisplayUtils.display_results(result)

        except Exception as e:
            print(f"An error occurred during the database query: {e}")
