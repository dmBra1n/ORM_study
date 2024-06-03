from models import TransactionsOrm, VisitsOrm
from sqlalchemy import func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class CustomerCore(BaseCore):
    def find_id_users(self):
        with self.session() as session:
            query = (
                """SELECT customer_id, COUNT(visit_id) AS count_no_trans
                FROM Visits
                WHERE visit_id NOT IN(SELECT visit_id FROM Transactions)
                GROUP BY customer_id;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class CustomerOrm(BaseOrm):
    def find_id_users(self):
        visits = aliased(VisitsOrm)
        transactions = aliased(TransactionsOrm)
        with self.session() as session:
            subq = (
                select(transactions.visit_id)
            )
            query = (
                select(
                    visits.customer_id,
                    func.count(visits.visit_id).label("count_no_trans")
                )
                .where(visits.visit_id.notin_(subq))
                .group_by(visits.customer_id)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
