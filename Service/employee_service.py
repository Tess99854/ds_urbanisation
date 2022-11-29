from sqlalchemy.orm import Session

from Model.Employee import Employee
from Schema.Employee import CreateEmployee
from Util.mysql_connector import MySQLConnection


def get_all(db: Session):
    employees = db.query(Employee).all()
    return employees


def create(employee: Employee):
    db = MySQLConnection.get_db()
    db.add(employee)
    db.commit()
    db.close()


def update(id, new_employee: Employee):
    db = MySQLConnection.get_db()
    employee = db.query(Employee).get(id)
    employee.firstName = new_employee['firstName']
    employee.lastName = new_employee['lastName']
    employee.salary = new_employee['salary']


def delete(id, db: Session):
    employee = get(id, db)
    db.delete(employee)
    db.commit()


def get(id, db: Session):
    employee = db.query(Employee).filter(Employee.id == id).first()
    return employee


def get_salary(id, currency: str, db: Session):
    employee = get(id, db)
    if currency.upper() == 'USD':
        return float(employee.salary)
    elif currency.upper() == 'EUR':
        return float(employee.salary) * 0.97
    else:
        return 0
