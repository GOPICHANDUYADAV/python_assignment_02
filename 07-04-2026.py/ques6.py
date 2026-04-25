#vechile hierarchy
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def info(self):
        return f"{self.year} {self.make} {self.model} with {self.num_doors} doors."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def info(self):
        if self.has_sidecar:
            return f"{self.year} {self.make} {self.model} with a sidecar."
        else:
            return f"{self.year} {self.make} {self.model} without a sidecar."


def print_vehicle_info(vehicle):
    print(vehicle.info())


# Test
car = Car("Toyota", "Camry", 2022, 4)
bike = Motorcycle("Harley-Davidson", "Sportster", 2021, True)

print_vehicle_info(car)
print_vehicle_info(bike)