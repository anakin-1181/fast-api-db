from fastapi import FastAPI

import fast_api_db.main

app = FastAPI()

# Using the original function
# app.get("/")(read_message)


# Overriding the imported function
@app.get("/")
def read_message():
    return {"Merry": "Christmas"}


print(fast_api_db.main.read_message())
