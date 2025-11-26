from basis import Basis


class Soldier(Basis):
    def __init__(self,personal_number,first_name,lest_name,gender,residential_city,distance_from_the_basis):
        self.personal_number = personal_number
        self.first_name = first_name
        self.lest_name = lest_name
        self.gender = gender
        self.residential_city =residential_city
        self.distance_from_the_basis =distance_from_the_basis