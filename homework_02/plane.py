"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo, max_cargo=None):
        self.cargo = cargo
        super().__init__(weight=100, started=10, fuel=20, fuel_consumption=10)
        self.max_cargo = max_cargo

    def load_cargo(self, mass: int):

        if self.cargo + mass <= self.max_cargo:
            self.cargo = self.cargo + mass
        else:
            raise CargoOverload("Sorry, Cargo Over load!")

    def remove_all_cargo(self):

        cargo, self.cargo = self.cargo, 0
        return cargo
