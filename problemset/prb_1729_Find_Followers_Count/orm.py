from models import FollowersOrm
from sqlalchemy import func, select
from sqlalchemy.orm import aliased

from utils.database import Base, session_factory, sync_engine
from utils.fetch_data import fetch_data_from_sql_query
from utils.sqlalchemy_helpers import DisplayUtils


class SyncOrm:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_followers(sql_file_path):
        try:
            with session_factory() as session:
                data = fetch_data_from_sql_query(sql_file_path)

                for row in data["data"]:
                    session.add(FollowersOrm(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def followers_count():
        with session_factory() as session:
            followers = aliased(FollowersOrm)
            query = (
                select(
                    followers.user_id,
                    func.count(followers.follower_id).label("followers_count")
                )
                .group_by(followers.user_id)
                .order_by(followers.user_id)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
