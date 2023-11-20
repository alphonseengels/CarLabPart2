class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def honk(self):
        print("HONK")


class Car(Vehicle):
   def __init__(self, make, model, year, weight, num_doors):
       super().__init__(make, model, year, weight)
       self.num_doors = num_doors

   def honk(self):
       print("BEEP!")

class Boat(Vehicle):
    def __init__(self, make, model, year, weight, boat_type):
        super().__init__(make, model, year, weight)
        self.boat_type = boat_type
    def honk(self):
        print("BOOOO-OOOO")

    def anchor(self):
        print("DROPPING ANCHOR... CLINK!")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, payload_capacity):
        super().__init__(make, model, year, weight)
        self.payload_capacity = payload_capacity

    def honk(self):
        print("BUAAAHHHH!")

    def dump_load(self):
        print("DUMPING LOAD... BOOM!")
