from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Numeric

from Util.mysql_connector import MySQLConnection

Base = MySQLConnection.get_base()


class Employee(Base):
    __tablename__ = "Employee"
    id = Column(Integer, primary_key=True)
    firstName = Column(String(20))
    lastName = Column(String(20))
    salary = Column(Numeric)
    pass
