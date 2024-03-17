from http import HTTPStatus
from src.services.repositories.employee_respository import EmployeeRepository

class employeeService():
    
    def __init__(self):
        self.repository = EmployeeRepository()
        
    def list(self):
        return self.repository.list_employees()