from fastapi import FastAPI ,UploadFile
from logik.stage_A import *
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csv_file:UploadFile):
    return text_to_object(csv_to_text(csv_file))


