from models import AddressOrm, PersonOrm
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class CombineTwoTablesCore(BaseCore):
    def combine_two_tables(self):
        with self.session() as session:
            query = (
                """SELECT p.firstName, p.lastName, a.city, a.state
                FROM Person p
                LEFT JOIN Address a ON p.personId = a.personId;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class CombineTwoTablesOrm(BaseOrm):
    def combine_two_tables(self):
        with self.session() as session:
            address = aliased(AddressOrm)
            person = aliased(PersonOrm)
            query = (
                select(
                    person.firstName,
                    person.lastName,
                    address.city,
                    address.state
                )
                .join(
                    address,
                    person.personId == address.personId,
                    isouter=True
                )
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
