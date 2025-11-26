import io
import csv
from nudals.soldier import Soldier
from nudals.bed import Bed

soldiers = []
waiting_list = []
beds = []

def csv_to_text(file):
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    next(reader)
    rows = list(reader)
    return rows

def text_to_object(text):
    for row in text:
        soldier_object = Soldier(row[0],row[1],row[2],row[3],row[4],row[5])
        soldiers.append(soldier_object)
    return soldiers


def create_waiting_list():
    for soldier in soldiers:
        if soldier.building_number is None :
            waiting_list.append(soldier)

def first_in_list(first ,long_distance):
    for item in waiting_list:
        if int(item.distance_from_the_basis) > int(long_distance):
            long_distance = item.distance_from_the_basis
            first = item
    waiting_list.remove(first)
    return first

def create_beds_list():
    for building in range(2):
        for room in range(10):
            for bed in range(8):
                beds.append(Bed(building +1 ,room +1 ,bed +1 ))

def assignment():
    first = None
    long_distance = 0
    for bed in range(len(beds)):
        first = first_in_list(first, long_distance)
        if beds[bed].soldier_number is None:
            beds[bed].soldier_number = first.personal_number
            first.building_number = beds[bed].building_number
            first.room_number = beds[bed].number_of_room


def return_result():
    pass



