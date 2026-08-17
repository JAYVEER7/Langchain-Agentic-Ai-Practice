from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str ='Nitish'
    age: Optional[int] =None
    email: EmailStr
    cgpa: float= Field(ft=0, lt= 10, dafault=5, description= " A decimal value is representing!!!")

# new_Student= {'name': 'JAY'}  # if we pass 20 instead of "JAY " then it would give error 

new_Student= {'age': 32, 'email': 'abs@gmail.com', 'cgpa':4}  
# new_Student= {'age': '32'}    ### it correct automatically, type cohering
student= Student(**new_Student)
print(student)

student_json= student.model_dump_json()