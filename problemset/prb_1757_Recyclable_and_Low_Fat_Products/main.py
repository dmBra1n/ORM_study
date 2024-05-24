from models import ProductsOrm, metadata_obj
from solving import (RecyclableAndLowFatProductsCore,
                     RecyclableAndLowFatProductsCoreOrm)

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = RecyclableAndLowFatProductsCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_products.sql")
    problem_core.find_products()

    problem_orm = RecyclableAndLowFatProductsCoreOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_products.sql", ProductsOrm)
    problem_orm.find_products()


if __name__ == '__main__':
    main()
