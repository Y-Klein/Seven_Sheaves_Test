from basis import Basis


class Bed(Basis):
    def __init__(self,building_number,number_of_room,number_of_bed, soldier_number = None):
        self.building_number = building_number
        self.number_of_room = number_of_room
        self.number_of_bed = number_of_bed
        self.soldier_number = soldier_number
