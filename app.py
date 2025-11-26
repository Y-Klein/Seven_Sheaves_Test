from fastapi import FastAPI ,UploadFile
from logik.stage_A import csv_to_text
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csv_file:UploadFile):
    return csv_to_text(csv_file)


