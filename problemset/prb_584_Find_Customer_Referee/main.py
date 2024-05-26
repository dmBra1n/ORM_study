from models import CustomerOrm, metadata_obj
from solving import FindCustomerRefereeCore, FindCustomerRefereeOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = FindCustomerRefereeCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_customer.sql")
    problem_core.find_names()

    problem_orm = FindCustomerRefereeOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_customer.sql", CustomerOrm)
    problem_orm.find_names()


if __name__ == '__main__':
    main()
