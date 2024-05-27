from models import WeatherOrm
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class RisingTemperatureCore(BaseCore):
    def get_higher_temperatures(self):
        with self.session() as session:
            query = (
                """SELECT w1.id
                FROM Weather w1
                JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1
                WHERE w1.temperature > w2.temperature;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class RisingTemperatureOrm(BaseOrm):
    def get_higher_temperatures(self):
        with self.session() as session:
            w1 = aliased(WeatherOrm)
            w2 = aliased(WeatherOrm)
            query = (
                select(w1.id)
                .join(w2, w1.recordDate == w2.recordDate + 1)
                .where(w1.temperature > w2.temperature)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
