from random import randint
from taxi import Car

class Unreliablecar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel,reliability)
        self.reliability = reliability

    def __str__(self):
        return "{}, {}km on current fare".format(super().__str__(), self.reliability)

    def drive(self, distance):
        start_drive = randint(0,100)
        if start_drive < self.reliability:
            distance_driven = super.drive(distance)
        else:
            print("You turned the key and it didn't move")
            distance_driven = 0
        return distance_driven