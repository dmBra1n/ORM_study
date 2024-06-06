from models import SalaryOrm, metadata_obj
from solving import SwapSalaryCore, SwapSalaryOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = SwapSalaryCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_salary.sql")
    problem_core.get_all_data_from_db()
    problem_core.update_data()
    problem_core.get_all_data_from_db()

    problem_orm = SwapSalaryOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_salary.sql", SalaryOrm)
    problem_orm.get_all_data_from_db()
    problem_orm.update()
    problem_orm.get_all_data_from_db()


if __name__ == '__main__':
    main()
