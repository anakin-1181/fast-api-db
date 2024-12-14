from fastapi import FastAPI, HTTPException

app = FastAPI()

sample_db = {1: "Alex", 2: "Betty", 3: "Carlos"}


@app.get("/")
def read_message():
    return {"Hello": "World"}


@app.get("/students/{student_id}")
def read_studentID(student_id: int) -> str:
    # My try on returning value from database ###

    # try:
    #     return sample_db[student_id]
    # except KeyError:
    #     return "Error: key not found"

    # Using HTTPException after researh ###

    if student_id in sample_db:
        return sample_db[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")
