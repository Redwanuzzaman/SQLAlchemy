from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import orm


employees_table = Table('employees', db.metaData,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('role', String(50)),
    Column('email', String(50)),
    Column('phone', Integer),
    Column('assigned_organization', String(50))
)


class Employee():
    pass


employee_mapper = orm.mapper(Employee, employees_table)
