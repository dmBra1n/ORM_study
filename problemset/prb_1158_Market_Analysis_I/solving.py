from models import OrdersOrm, UsersOrm
from sqlalchemy import and_, func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class MarketAnalysisCore(BaseCore):
    def find_users(self):
        with self.session() as session:
            query = (
                """SELECT u.user_id AS buyer_id,
                u.join_date AS join_date,
                COUNT(o.buyer_id) AS orders_in_2019
                FROM Users u LEFT JOIN Orders o
                ON u.user_id = o.buyer_id
                AND EXTRACT(YEAR FROM order_date) = 2019
                GROUP BY u.user_id
                ORDER BY u.user_id;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class MarketAnalysisOrm(BaseOrm):
    def find_users(self):
        with self.session() as session:
            users = aliased(UsersOrm)
            orders = aliased(OrdersOrm)
            query = (
                select(
                    users.user_id.label("buyer_id"),
                    users.join_date,
                    func.count(orders.buyer_id).label("orders_in_2019")
                )
                .join(
                    orders,
                    and_(
                        users.user_id == orders.buyer_id,
                        func.extract("year", orders.order_date) == 2019
                    ),
                    isouter=True
                )
                .group_by(users.user_id)
                .order_by(users.user_id)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
