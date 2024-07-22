from sqlalchemy.orm import Session
from . import models, schemas

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()

def update_department(db: Session, department_id: int, department: schemas.DepartmentCreate):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    for key, value in department.dict().items():
        setattr(db_department, key, value)
    db.commit()
    db.refresh(db_department)
    return db_department

def delete_department(db: Session, department_id: int):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    db.delete(db_department)
    db.commit()
    return db_department

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    old_department_id = db_employee.department_id
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee, old_department_id

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    db.delete(db_employee)
    db.commit()
    return db_employee

def update_department_employee_count(db: Session, department_id: int, increment: bool = True):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    if increment:
        db_department.number_of_employees += 1
    else:
        db_department.number_of_employees -= 1
    db.commit()
