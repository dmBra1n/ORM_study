from models import StocksOrm, metadata_obj
from solving import CapitalGainLossCore, CapitalGainLossOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = CapitalGainLossCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_stocks.sql")
    problem_core.capital_gain_loss()

    problem_orm = CapitalGainLossOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_stocks.sql", StocksOrm)
    problem_orm.capital_gain_loss()


if __name__ == '__main__':
    main()
