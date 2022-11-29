from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from Schema.Employee import Employee as EmployeeSchema, CreateEmployee
from typing import List

from Service import employee_service
from Util.mysql_connector import MySQLConnection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def get_db():
    try:
        db_object = MySQLConnection.get_session()
        db = db_object()
        yield db
    finally:
        db.close()


@app.get("/employees", response_model=List[EmployeeSchema])
async def get_all(db: Session = Depends(get_db)):
    employees = employee_service.get_all(db)
    return employees


@app.get("/employees/{id}", response_model=EmployeeSchema)
async def get(id: int, db: Session = Depends(get_db)):
    employee = employee_service.get(id, db)
    return employee


@app.post("/employees/")
async def create(new_employee: EmployeeSchema):
    employee_service.create(new_employee)


@app.put("/employees/{id}")
async def update(id: int, updated_employee: EmployeeSchema):
    employee_service.update(id, updated_employee)


@app.get("/employees/{id}/salary/{currency}")
async def get_salary(id: int, currency: str, db: Session = Depends(get_db)):
    return employee_service.get_salary(id, currency, db)
