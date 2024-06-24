from models import AddressOrm, PersonOrm, metadata_obj
from solving import CombineTwoTablesCore, CombineTwoTablesOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = CombineTwoTablesCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_person.sql")
    problem_core.insert_data("insert_data_into_address.sql")
    problem_core.combine_two_tables()

    problem_orm = CombineTwoTablesOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_person.sql", PersonOrm)
    problem_orm.insert_data("insert_data_into_address.sql", AddressOrm)
    problem_orm.combine_two_tables()


if __name__ == '__main__':
    main()
