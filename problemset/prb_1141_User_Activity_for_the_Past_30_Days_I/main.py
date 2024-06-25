from models import ActivityOrm, metadata_obj
from solving import UserActivityCore, UserActivityOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = UserActivityCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_activity.sql")
    problem_core.find_active_user()

    problem_orm = UserActivityOrm(
        base=Base,
        session=session_factory,
        engine=sync_engine
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_activity.sql", ActivityOrm)
    problem_orm.find_active_user()


if __name__ == '__main__':
    main()
