from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
students = {
    1: {"name": "John", "age": 18, "grade": 12, "major": "Physics"},
    2: {"name": "Emma", "age": 17, "grade": 11, "major": "Biology"},
    3: {"name": "Michael", "age": 16, "grade": 10, "major": "History"},
    4: {"name": "Sophia", "age": 18, "grade": 12, "major": "Chemistry"},
    5: {"name": "William", "age": 17, "grade": 11, "major": "Mathematics"},
    6: {"name": "Olivia", "age": 16, "grade": 10, "major": "English"},
    7: {"name": "James", "age": 18, "grade": 12, "major": "Computer Science"},
    8: {"name": "Amelia", "age": 17, "grade": 11, "major": "Psychology"},
    9: {"name": "Alexander", "age": 16, "grade": 10, "major": "Sociology"},
    10: {"name": "Isabella", "age": 18, "grade": 12, "major": "Geography"},
    11: {"name": "Ethan", "age": 17, "grade": 11, "major": "Economics"},
    12: {"name": "Mia", "age": 16, "grade": 10, "major": "Political Science"},
    13: {"name": "Daniel", "age": 18, "grade": 12, "major": "Art"},
    14: {"name": "Ava", "age": 17, "grade": 11, "major": "Music"},
    15: {"name": "Matthew", "age": 16, "grade": 10, "major": "Drama"},
    16: {"name": "Emily", "age": 18, "grade": 12, "major": "Health Education"},
    17: {"name": "Ryan", "age": 17, "grade": 11, "major": "Physical Education"},
    18: {"name": "Charlotte", "age": 16, "grade": 10, "major": "Nutrition"},
    19: {"name": "David", "age": 18, "grade": 12, "major": "Engineering"},
    20: {"name": "Samantha", "age": 17, "grade": 11, "major": "Architecture"},
}

class Student(BaseModel):
    name: str
    age: int
    grade: int
    major: str


@app.get("/")
def index():
    return {'name':'first data'}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='The ID of the student you want to view')):

    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name: Optional[str] =None, test: int):
    for student_id in students:
        if students[student_id]['name']==name:
            return students[student_id]
        
    return {'data':'not found'}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:Student):
    if student_id in students:
        return {'error':'Student exists'}
    students[student_id]=student
    return students[student_id]