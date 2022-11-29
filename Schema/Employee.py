import decimal

from pydantic import BaseModel


class CreateEmployee(BaseModel):
    firstName: str
    lastName: str
    salary: decimal.Decimal

    class Config:
        orm_mode = True


class Employee(CreateEmployee):
    id: int

    class Config:
        orm_mode = True