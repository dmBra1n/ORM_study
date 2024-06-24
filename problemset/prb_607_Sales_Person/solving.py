from models import CompanyModel, OrdersModel, SalesPersonModel
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class SalesPersonCore(BaseCore):
    def find_sales_persons(self):
        with self.session() as session:
            query = (
                """SELECT name
                FROM SalesPerson
                WHERE sales_id NOT IN(
                    SELECT sales_id
                    FROM Company c JOIN Orders o ON c.com_id = o.com_id
                    WHERE c.name = 'RED'
                    );"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class SalesPersonOrm(BaseOrm):
    def find_sales_persons(self):
        with self.session() as session:
            sales_person = aliased(SalesPersonModel)
            orders = aliased(OrdersModel)
            company = aliased(CompanyModel)
            subq = (
                select(orders.sales_id)
                .join(company, company.com_id == orders.com_id, isouter=True)
                .where(company.name == "RED")
                .subquery()
            )
            query = (
                select(sales_person.name)
                .where(sales_person.sales_id.notin_(select(subq)))
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
