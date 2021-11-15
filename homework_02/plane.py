"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):

        self.cargo = cargo
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, mass: int):

        if mass + self.cargo > self.max_cargo:
            raise CargoOverload("Sorry, Cargo Over load!")
        else:
            self.cargo = self.cargo + mass

    def remove_all_cargo(self):

        cargo, self.cargo = self.cargo, 0
        return cargo
