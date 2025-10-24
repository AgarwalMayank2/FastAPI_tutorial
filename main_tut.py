from fastapi import FastAPI

app = FastAPI() ## Our FastAPI instance for handling the requests

@app.get("/") ## Get request from the user and respond something in the "/" page that is the homepage.
def simple_response():
    return "This is a simple non-parameterized response"

@app.get("/status")
def student_status(name, roll_number, gender):
    pass