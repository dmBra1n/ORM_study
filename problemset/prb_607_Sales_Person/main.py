from models import CompanyModel, OrdersModel, SalesPersonModel, metadata_obj
from solving import SalesPersonCore, SalesPersonOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = SalesPersonCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_sales_person.sql")
    problem_core.insert_data("insert_data_into_company.sql")
    problem_core.insert_data("insert_data_into_orders.sql")
    problem_core.find_sales_persons()

    problem_orm = SalesPersonOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data(
        "insert_data_into_sales_person.sql", SalesPersonModel
    )
    problem_orm.insert_data("insert_data_into_company.sql", CompanyModel)
    problem_orm.insert_data("insert_data_into_orders.sql", OrdersModel)
    problem_orm.find_sales_persons()


if __name__ == '__main__':
    main()
