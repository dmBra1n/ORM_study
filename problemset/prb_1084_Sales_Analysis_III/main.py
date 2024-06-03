from models import ProductOrm, SalesOrm, metadata_obj
from solving import SalesAnalysisCore, SalesAnalysisOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = SalesAnalysisCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_product.sql")
    problem_core.insert_data("insert_data_into_sales.sql")
    problem_core.find_products()

    problem_orm = SalesAnalysisOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_product.sql", ProductOrm)
    problem_orm.insert_data("insert_data_into_sales.sql", SalesOrm)
    problem_orm.find_products()


if __name__ == '__main__':
    main()
