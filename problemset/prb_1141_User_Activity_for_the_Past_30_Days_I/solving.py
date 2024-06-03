from models import ActivityOrm
from sqlalchemy import func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class UserActivityCore(BaseCore):
    def find_active_user(self):
        with self.session() as session:
            query = (
                """SELECT activity_date AS day,
                        COUNT(DISTINCT user_id) AS active_users
                    FROM Activity
                    WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
                    GROUP BY activity_date;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class UserActivityOrm(BaseOrm):
    def find_active_user(self):
        with self.session() as session:
            activity = aliased(ActivityOrm)
            query = (
                select(
                    activity.activity_date.label("day"),
                    func.count(
                        activity.user_id.distinct()
                    ).label("active_users")
                )
                .where(activity.activity_date.between(
                    func.date('2019-06-28'),
                    func.date('2019-07-27')
                ))
                .group_by(activity.activity_date)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
