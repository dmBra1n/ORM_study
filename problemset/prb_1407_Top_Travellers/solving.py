from models import RidesOrm, UsersOrm
from sqlalchemy import desc, func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class TopTravellersCore(BaseCore):
    def top_travellers(self):
        with self.session() as session:
            query = (
                """SELECT u.name,
                    COALESCE(SUM(r.distance), 0) AS travelled_distance
                    FROM Users u LEFT JOIN Rides r ON u.id = r.user_id
                    GROUP BY u.id, u.name
                    ORDER BY travelled_distance DESC, u.name;""")
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class TopTravellersOrm(BaseOrm):
    def top_travellers(self):
        with self.session() as session:
            users = aliased(UsersOrm)
            rides = aliased(RidesOrm)
            query = (
                select(
                    users.name,
                    func.coalesce(
                        func.sum(rides.distance), 0
                    ).label("travelled_distance")
                )
                .join(rides, users.id == rides.user_id, isouter=True)
                .group_by(users.id)
                .order_by(desc("travelled_distance"), users.name)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
