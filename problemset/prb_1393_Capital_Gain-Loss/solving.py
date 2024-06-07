from models import StocksOrm
from sqlalchemy import case, func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class CapitalGainLossCore(BaseCore):
    def capital_gain_loss(self):
        with self.session() as session:
            query = (
                """SELECT stock_name, SUM(
                        CASE
                        WHEN operation = 'Buy' THEN -price
                        WHEN operation = 'Sell' THEN price
                        END
                        ) AS capital_gain_loss
                    FROM Stocks
                    GROUP BY stock_name;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class CapitalGainLossOrm(BaseOrm):
    def capital_gain_loss(self):
        with self.session() as session:
            stocks = aliased(StocksOrm)
            query = (
                select(
                    stocks.stock_name,
                    func.sum(
                        case(
                            (stocks.operation == 'Buy', -stocks.price),
                            (stocks.operation == 'Sell', stocks.price)
                        )
                    ).label("capital_gain_loss")
                )
                .group_by(stocks.stock_name)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
