from fastapi import FastAPI, Path, Query

app = FastAPI() ## Our FastAPI instance for handling the requests

@app.get("/") ## Get request from the user and respond something in the "/" page that is the homepage.
def simple_response():
    return "This is a simple non-parameterized response"

sample_database = [
    {"name": "XYZ", "roll no.": "B29CM65", "gender": "male", "subjects enrolled": "PCS, OML, DE, DAA, AI, PRML", "CGPA":8.91},
    {"name": "ABC", "roll no.": "B29CS23", "gender": "female", "subjects enrolled": "DBMS, DAA, OS, POPL, COA, PRML", "CGPA":7.72}
]

@app.get("/status")
def student_status(name = Query(None, description="Enter name of the student"), roll_number = Query(None, description="Enter roll number of the student"), gender = Query(None, description="Enter gender of the student")):
## The parameters in this function are query parameters and not path parameters as they are not required in the URL and that is why we can have a default value
## of None in here. If it would have been a path parameter(use "Path" in place of "Query") then we cannot have None as default value
    for student in sample_database:
        if student["roll no."] == roll_number:
            return student
    return "Student not found"

@app.post("/create_student") ## Works same as GET but according to REST principles, we use this for new data
def create_student(new_student: dict):
    for student in sample_database:
        if student == new_student:
            return "Student already exists"
    sample_database.append(new_student)
    return "Student added"

## Likewise, according to REST principles, we use 'put' for update and 'delete' for delete operations

@app.put("/modify_student")
def update(roll_number : str = Query(None)):
    pass

@app.delete("/delete_student")
def delete(roll_number : str = Query(None)):
    pass