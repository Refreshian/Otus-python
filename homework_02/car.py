"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    engine = None

    def set_engine(self, engine):
        self.engine = engine

# X = Car(1, 2, 3, 4).set_engine(6)
