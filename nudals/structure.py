from basis import Basis


class Structure(Basis):
    def __init__(self,building_number,number_of_rooms,number_of_beds_per_room):
        self.building_number = building_number
        self.number_of_rooms = number_of_beds_per_room
        self.number_of_beds_per_room = number_of_beds_per_room
