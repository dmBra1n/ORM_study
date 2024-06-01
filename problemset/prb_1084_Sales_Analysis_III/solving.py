from models import ProductOrm, SalesOrm
from sqlalchemy import and_, func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class SalesAnalysisCore(BaseCore):
    def find_products(self):
        with self.session() as session:
            query = (
                """SELECT product_id, product_name
                    FROM Product
                    WHERE product_id IN(
                        SELECT product_id
                        FROM Sales
                        GROUP BY product_id
                        HAVING MIN(sale_date) >= '2019-01-01'
                            AND MAX(sale_date) <= '2019-03-31'
                        )"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class SalesAnalysisOrm(BaseOrm):
    def find_products(self):
        with self.session() as session:
            product = aliased(ProductOrm)
            sales = aliased(SalesOrm)
            subq = (
                select(sales.product_id)
                .group_by(sales.product_id)
                .having(
                    and_(
                        func.min(sales.sale_date) >= func.date('2019-01-01'),
                        func.max(sales.sale_date) <= func.date('2019-03-31')
                    )
                )
                .subquery()
            )
            query = (
                select(product.product_id, product.product_name)
                .filter(product.product_id.in_(select(subq)))
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
