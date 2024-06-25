from models import DailySalesModel
from sqlalchemy import func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class DailyLeadsAndPartnersCore(BaseCore):
    def find_daily_lead_and_partner(self):
        with self.session() as session:
            query = (
                """SELECT
                        date_id,
                        make_name,
                        COUNT(DISTINCT lead_id) AS unique_leads,
                        COUNT(DISTINCT partner_id) AS unique_partners
                    FROM DailySales
                    GROUP BY date_id, make_name;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class DailyLeadsAndPartnersOrm(BaseOrm):
    def find_daily_lead_and_partner(self):
        with self.session() as session:
            daily_sales = aliased(DailySalesModel)
            query = (
                select(
                    daily_sales.date_id,
                    daily_sales.make_name,
                    func.count(
                        daily_sales.lead_id.distinct()
                    ).label("unique_leads"),
                    func.count(
                        daily_sales.partner_id.distinct()
                    ).label("unique_partners")
                )
                .group_by(daily_sales.date_id, daily_sales.make_name)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
