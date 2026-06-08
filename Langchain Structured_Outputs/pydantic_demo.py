from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name: str = 'Abdullah'
    age: Optional[int] = None
    email: EmailStr = None
    cgpa: float = Field(gt=0, lt=10, default = None, description="CGPA of a student")
    
new_student = {'age' : 23}

std = Student(**new_student)

student_dict = dict(std)
print(student_dict)
print(student_dict['age'])

student_json = std.model_dump_json()

print(student_json)