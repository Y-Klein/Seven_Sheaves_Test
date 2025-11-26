from fastapi import FastAPI ,UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/assignWithCsv")
def upload_csv(csvFile:UploadFile):
    return "file uploaded"


