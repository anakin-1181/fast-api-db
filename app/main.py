from fastapi import FastAPI
from fast_api_db.utils import abc

# attempt to replace the output of read_message
# from src.fast_api_db.main import read_message

app = FastAPI()

# Using the original function
# app.get("/")(read_message)


# Overriding the imported function
@app.get("/")
def read_message():
    return {"Merry": "Christmas", "payload": abc()}
