# CRUD-FastAPI

This project implements a CRUD (Create, Read, Update, Delete) API for managing employees and departments using SQLAlchemy, a powerful ORM (Object-Relational Mapping) library for Python. 
The project provides endpoints to interact with a relational database, allowing users to perform operations such as creating, retrieving, updating, and deleting records for employees and departments.

# Setup Instructions

  -> Create a directory, open cmd in directory path  and clone Vendor-Navigator project
  
      https://github.com/abynxv/CRUD-FastAPI.git

  -> Install Virtual environment
  
      pip install virtualenv

  -> Create virtual environment within the directory. 
  
      python -m venv venv_name  # On Windows
      python3 -m venv venv_name  # On macOS/Linux

  -> Activate virtual environmant    
  
      venv_name\Scripts\activate       # On Windows           
      source venv_name/bin/activate     # On macOS/Linux

  -> Install requirements.txt
  
      pip install -r requirements.txt

  -> Open Project in VScode
 
      code .

  -> Open terminal in vscode, navigate to project directory, Run the server and follow link

      cd fastapi_project
      uvicorn app.main:app --reload


# FastAPI-CRUD Project: API Endpoints

Department

1.Create a Department

    Endpoint    : POST /departments/
    Description : Create a new department.
    Request Body:
          {
            "name"                : "string",
            "number_of_employees" : 0
          }
    Response    :
          {
            "id"                  : "integer",
            "name"                : "string",
            "number_of_employees" : "integer"
          }

2.Get a Department by ID

    Endpoint    : GET /departments/{department_id}
    Description : Retrieve a department by its ID.
    Response    :
          {
            "id"                  : "integer",
            "name"                : "string",
            "number_of_employees" : "integer"
          }

3.Get All Departments

    Endpoint    : GET /departments/
    Description : Retrieve a list of all departments.
    Query Parameters :
        skip         : Integer, number of records to skip (default: 0)
        limit        : Integer, maximum number of records to return (default: 100)
    Response    :
        [
          {  
            "id"                  : "integer",
            "name"                : "string",
            "number_of_employees" : "integer"
          }
        ]

4.Update a Department by ID

    Endpoint    : PUT /departments/{department_id}
    Description : Update an existing department by its ID.
    Request Body:
          {
            "name"                : "string",
            "number_of_employees" : "integer"
          }

    Response    :  
          {
            "id"                  : "integer",
            "name"                : "string",
            "number_of_employees" : "integer"
          }
5.Delete a Department by ID

    Endpoint    : DELETE /departments/{department_id}
    Description : Delete a department by its ID.
    Response    :
          {
            "id"                  : "integer",
            "name"                : "string",
            "number_of_employees" : "integer"
          }

Employees

1.Create an Employee

    Endpoint    : POST /employees/
    Description : Create a new employee.
    Request Body:
          {
            "name"          : "string",
            "department_id" : "integer"
          }
    Response:
          {
            "id"            : "integer",
            "name"          : "string",
            "department_id" : "integer"
          }

2.Get an Employee by ID

    Endpoint    : GET /employees/{employee_id}
    Description : Retrieve an employee by its ID.
    Response    :
          {
            "id"            : "integer",
            "name"          : "string",
            "department_id" : "integer"
          }

3.Get All Employees

    Endpoint    : GET /employees/
    Description : Retrieve a list of all employees.
    Query Parameters :
        skip         : Integer, number of records to skip (default: 0)
        limit        : Integer, maximum number of records to return (default: 100)
    Response    :
        [
          {
            "id"            : "integer",
            "name"          : "string",
            "department_id" : "integer"
          }
        ]

4.Update an Employee by ID

    Endpoint    : PUT /employees/{employee_id}
    Description : Update an existing employee by its ID.
    Request Body:
          {
            "name"          : "string",
            "department_id" : "integer"
          }

    Response    :
          {
            "id"            : "integer",
            "name"          : "string",
            "department_id" : "integer
          }

5.Delete an Employee by ID

    Endpoint    : DELETE /employees/{employee_id}
    Description : Delete an employee by its ID.
    Response    :
          {
            "id"            : "integer",
            "name"          : "string",
            "department_id" : "integer"
          }
