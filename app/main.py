from fastapi import FastAPI

import fast_api_db.utils as utils

# attempt to replace the output of read_message
# from src.fast_api_db.main import read_message

app = FastAPI()


@app.get("/")
def utils_function():
    return {"message": utils.dummy_function}
