from pydantic import BaseModel
from datetime import date

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    number_of_employees: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    gender: str
    date_of_birth: date
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True