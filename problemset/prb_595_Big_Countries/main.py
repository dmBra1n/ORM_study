from models import WorldOrm, metadata_obj
from solving import BigCountriesCore, BigCountriesOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = BigCountriesCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_world.sql")
    problem_core.get_big_country()

    problem_orm = BigCountriesOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_world.sql", WorldOrm)
    problem_orm.get_big_country()


if __name__ == '__main__':
    main()
