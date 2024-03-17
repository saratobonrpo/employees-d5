from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeBase(BaseModel):
    employee_name: str
    employee_email: str
    phone: str  
    job_title: str 
    hire_date: date 


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "employee_name": self.employee_name,
    #         "employee_email": self.employee_email,
    #         "phone": self.phone,
    #         "job_title": self.job_title,
    #         "hire_date": self.hire_date.isoformat() if self.hire_date else None
    #     }
