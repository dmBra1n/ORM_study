from models import EmployeeOrm, metadata_obj
from solving import SecondHighestSalaryCore, SecondHighestSalaryOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = SecondHighestSalaryCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_employee.sql")
    problem_core.find_the_second_highest_salary()

    problem_orm = SecondHighestSalaryOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_employee.sql", EmployeeOrm)
    problem_orm.find_the_second_highest_salary()


if __name__ == '__main__':
    main()
