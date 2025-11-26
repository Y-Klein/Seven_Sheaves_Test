from fastapi import FastAPI ,UploadFile
from logik.stage_A import *
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csv_file:UploadFile):
    text_to_object(csv_to_text(csv_file))
    create_beds_list()
    create_waiting_list()
    assignment()
    return beds


