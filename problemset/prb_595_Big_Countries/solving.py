from models import WorldOrm
from sqlalchemy import or_, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class BigCountriesCore(BaseCore):
    def get_big_country(self):
        with self.session() as session:
            query = (
                """SELECT name, population, area
                FROM World
                WHERE population >= 25000000 OR area >= 3000000;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class BigCountriesOrm(BaseOrm):
    def get_big_country(self):
        with self.session() as session:
            world = aliased(WorldOrm)
            query = (
                select(world.name, world.population, world.area)
                .where(or_(
                    world.population >= 25000000,
                    world.area >= 3000000
                ))
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
