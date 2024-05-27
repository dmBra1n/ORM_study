from models import WeatherOrm, metadata_obj
from solving import RisingTemperatureCore, RisingTemperatureOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = RisingTemperatureCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_weather.sql")
    problem_core.get_higher_temperatures()

    problem_orm = RisingTemperatureOrm(
        base=Base,
        session=session_factory,
        engine=sync_engine
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_weather.sql", WeatherOrm)
    problem_orm.get_higher_temperatures()


if __name__ == '__main__':
    main()
