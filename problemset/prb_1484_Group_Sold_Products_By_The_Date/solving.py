from models import ActivitiesModel
from sqlalchemy import func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class GroupSoldProductsCore(BaseCore):
    def find_products_sold(self):
        with self.session() as session:
            query = (
                """SELECT sell_date,
                        COUNT(DISTINCT product) AS num_sold,
                        string_agg(DISTINCT product, ',') AS products
                    FROM Activities
                    GROUP BY 1
                    ORDER BY 1;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class GroupSoldProductsOrm(BaseOrm):
    def find_products_sold(self):
        with self.session() as session:
            activities = aliased(ActivitiesModel)
            query = (
                select(
                    activities.sell_date,
                    func.count(
                        activities.product.distinct()
                    ).label("num_sold"),
                    func.string_agg(
                        activities.product.distinct(), ","
                    ).label("products")
                )
                .group_by(activities.sell_date)
                .order_by(activities.sell_date)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
