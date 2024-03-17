from flask import Blueprint, request, jsonify, make_response
from http import HTTPStatus
from src.services.employeeService import employeeService
from src.models.models import Employee 

employees_controller = Blueprint('employee_routes', __name__)

@employees_controller.route('/', methods=['GET'], strict_slashes=False)
def get_employees():
    
    employee_services = employeeService()
    employees = employee_services.list()
    
    if employees is not None:
    
        return {"Employees": employees}, HTTPStatus.OK
    else:
        return {
                "Mensaje": "No se pudo actualizar la tarea con el Id:",
            }, HTTPStatus.BAD_REQUEST
        
employee_routes_blueprint = employees_controller