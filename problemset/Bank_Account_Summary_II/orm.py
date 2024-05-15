from models import TransactionsOrm, UsersOrm
from sqlalchemy import func, select
from sqlalchemy.orm import aliased

from utils.database import Base, session_factory, sync_engine
from utils.fetch_data import fetch_data_from_sql_query


class SyncOrm:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_users(sql_file_path):
        try:
            with session_factory() as session:
                data = fetch_data_from_sql_query(sql_file_path)

                for row in data["data"]:
                    session.add(UsersOrm(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def insert_transactions(sql_file_path):
        try:
            with session_factory() as session:
                data = fetch_data_from_sql_query(sql_file_path)

                for row in data["data"]:
                    session.add(TransactionsOrm(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def bank_account_summary():
        with session_factory() as session:
            u = aliased(UsersOrm)
            t = aliased(TransactionsOrm)
            query = (
                select(u.name, func.sum(t.amount))
                .join(t, u.account == t.account)
                .group_by(u.account)
                .having(func.sum(t.amount) > 10000)
            )

            res = session.execute(query)
            result = res.all()
            print(result)
