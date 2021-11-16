from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low Fuel Error!")

    def move(self, distance):

        if self.fuel // self.fuel_consumption >= distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel("Not Enough Fuel!")


# X = Vehicle(1000, 30, 4)
# print(X.move(10))
