from models import TransactionsOrm, VisitsOrm, metadata_obj
from solving import CustomerCore, CustomerOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = CustomerCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_visits.sql")
    problem_core.insert_data("insert_data_into_transactions.sql")
    problem_core.find_id_users()

    problem_orm = CustomerOrm(
        base=Base,
        session=session_factory,
        engine=sync_engine
    )
    problem_orm.create_tables()
    problem_orm.insert_data(
        "insert_data_into_visits.sql", orm_class=VisitsOrm
    )
    problem_orm.insert_data(
        "insert_data_into_transactions.sql", orm_class=TransactionsOrm
    )
    problem_orm.find_id_users()


if __name__ == '__main__':
    main()
