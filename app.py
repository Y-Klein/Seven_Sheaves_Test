from fastapi import FastAPI ,UploadFile
from logik.stage_A import *
from  logik.stage_B import *
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csv_file:UploadFile):
    result = return_result(csv_file)
    return result

@app.get("/space")
def occupancy_by_house():
    return select()
