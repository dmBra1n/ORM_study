from models import ItemsOrm, OrdersOrm, UsersOrm, metadata_obj
from solving import MarketAnalysisCore, MarketAnalysisOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = MarketAnalysisCore(
        metadata=metadata_obj,
        engine=sync_engine,
        session=session_factory
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_users.sql")
    problem_core.insert_data("insert_data_into_items.sql")
    problem_core.insert_data("insert_data_into_orders.sql")
    problem_core.find_users()

    problem_orm = MarketAnalysisOrm(
        base=Base,
        engine=sync_engine,
        session=session_factory
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_users.sql", UsersOrm)
    problem_orm.insert_data("insert_data_into_items.sql", ItemsOrm)
    problem_orm.insert_data("insert_data_into_orders.sql", OrdersOrm)
    problem_orm.find_users()


if __name__ == '__main__':
    main()
