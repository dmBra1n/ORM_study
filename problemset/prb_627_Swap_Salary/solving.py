from models import SalaryOrm, Sex
from sqlalchemy import String, case, cast, literal_column, select, text, update

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class SwapSalaryCore(BaseCore):
    def get_all_data_from_db(self):
        with self.session() as session:
            query = (
                """SELECT * FROM Salary;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)

    def update_data(self):
        with self.session() as session:
            stmt = (
                """UPDATE Salary
                    SET sex = CASE
                        WHEN sex = 'f' THEN 'm'::sex
                        ELSE 'f'::sex
                        END;"""
            )
            session.execute(text(stmt))
            session.commit()


class SwapSalaryOrm(BaseOrm):
    def get_all_data_from_db(self):
        with self.session() as session:
            query = (
                select(
                    SalaryOrm.id,
                    SalaryOrm.name,
                    cast(SalaryOrm.sex, String).label('sex'),
                    SalaryOrm.salary
                )
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)

    def update(self):
        with self.session() as session:
            sex_case = case(
                (
                    SalaryOrm.sex == Sex.f,
                    cast(literal_column("'m'"), SalaryOrm.sex.type)
                ),
                (
                    SalaryOrm.sex == Sex.m,
                    cast(literal_column("'f'"), SalaryOrm.sex.type)
                )
            )
            stmt = (
                update(SalaryOrm)
                .values(sex=sex_case)
            )
            session.execute(stmt)
            session.commit()
