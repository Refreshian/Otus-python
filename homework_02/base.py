from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=100, started=False, fuel=20, fuel_consumption=10):
        self.started = started
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, fuel, started=None):
        if not self.started:
            try:
                if self.fuel > 0:
                    self.started = True
            except Exception as e:
                raise LowFuelError("Sorry, Low Fuel Error!")

    def move(self, distance=None):
        if distance is not None:
            if self.fuel * self.fuel_consumption >= distance:
                self.fuel = self.fuel - distance / self.fuel_consumption
            else:
                raise NotEnoughFuel("Sorry, Not Enough Fuel!")
        else:
            print('Enter the distance!')
