import io
import csv
from nudals.soldier import Soldier
from nudals.bed import Bed

items = []
waiting_list = []
beds = []
long_distance = 0
first = None

def csv_to_text(file):
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    next(reader)
    rows = list(reader)
    return rows

def text_to_object(text):
    for row in text:
        soldier_object = Soldier(row[0],row[1],row[2],row[3],row[4],row[5])
        items.append(soldier_object)
    return items


def create_waiting_list():
    for item in items:
        if item.building_number is None :
            waiting_list.append(item)

def first_in_list():
    for item in waiting_list:
        if item.distance_from_the_basis > long_distance:
            long_distance = item.distance_from_the_basis
            first= item

def create_beds_list():
    for building in range(2):
        for room in range(10):
            for bed in range(8):
                beds.append(Bed(building,room,bed))

def assignment():
    while len(beds) > 0:
        first_in_list()
        for bed in beds:
            if bed.soldier_number is None:
                bed.soldier_number = first.personal_number
                beds.remove(bed)


def return_result():
    pass



