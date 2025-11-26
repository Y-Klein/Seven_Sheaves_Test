import io
import csv


def csv_to_text(file):
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    rows = list(reader)

    return rows


def assignment():
    pass

def return_result():
    pass



