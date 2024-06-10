from models import ActivitiesModel, metadata_obj
from solving import GroupSoldProductsCore, GroupSoldProductsOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = GroupSoldProductsCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_activities.sql")
    problem_core.find_products_sold()

    problem_orm = GroupSoldProductsOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_activities.sql", ActivitiesModel)
    problem_orm.find_products_sold()


if __name__ == '__main__':
    main()
