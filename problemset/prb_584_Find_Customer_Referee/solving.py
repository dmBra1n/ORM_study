from models import CustomerOrm
from sqlalchemy import or_, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class FindCustomerRefereeCore(BaseCore):
    def find_names(self):
        with self.session() as session:
            query = (
                """SELECT name
                FROM Customer
                WHERE referee_id != 2 OR referee_id is NULL"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class FindCustomerRefereeOrm(BaseOrm):
    def find_names(self):
        with self.session() as session:
            customer = aliased(CustomerOrm)
            query = (
                select(customer.name)
                .where(or_(
                    customer.referee_id != 2,
                    customer.referee_id.is_(None)
                ))
            )

            result = session.execute(query)
            DisplayUtils.display_results(result)
