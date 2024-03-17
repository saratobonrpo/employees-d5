from src.database.db import DatabaseManager

class EmployeeRepository():
    def __init__(self):
        self.connection = DatabaseManager()
        
    def list_employees(self):
        
        sql_query = "SELECT * FROM employees"
        
        response = self.connection.execute_query(sql_query)
        
        employees = []  
        
        for row in response:
            employee = {
                'employee_name	' : row[0],
                'employee_email' : row[1],
                'phone' : row[2],
                'job_title' : row[3],
                'hire_date' : row[4]
            }
            employees.append(employee)
        return employees