from fastapi import FastAPI ,UploadFile
from logik.stage_A import *
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csv_file:UploadFile):
    result = return_result(csv_file)
    return result


