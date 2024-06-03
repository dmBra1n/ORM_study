from models import EmployeeOrm
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class SecondHighestSalaryCore(BaseCore):
    def find_the_second_highest_salary(self):
        with self.session() as session:
            query = (
                """SELECT (
                    SELECT DISTINCT salary
                    FROM Employee
                    ORDER BY salary DESC
                    LIMIT 1
                    OFFSET 1
                ) AS "SecondHighestSalary";"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class SecondHighestSalaryOrm(BaseOrm):
    def find_the_second_highest_salary(self):
        with self.session() as session:
            employee = aliased(EmployeeOrm)
            query = (
                select(
                    employee.salary.distinct().label("SecondHighestSalary")
                )
                .order_by(employee.salary.desc())
                .limit(1)
                .offset(1)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
