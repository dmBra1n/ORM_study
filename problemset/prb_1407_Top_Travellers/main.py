from models import RidesOrm, UsersOrm, metadata_obj
from solving import TopTravellersCore, TopTravellersOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = TopTravellersCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_users.sql")
    problem_core.insert_data("insert_data_into_rides.sql")
    problem_core.top_travellers()

    problem_orm = TopTravellersOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_users.sql", UsersOrm)
    problem_orm.insert_data("insert_data_into_rides.sql", RidesOrm)
    problem_orm.top_travellers()


if __name__ == '__main__':
    main()
