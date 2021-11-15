"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass
# raise LowFuelError("Sorry, Low Fuel Error!")


class NotEnoughFuel(Exception):
    pass
# raise NotEnoughFuel("Sorry, Not Enough Fuel!")


class CargoOverload(Exception):
    pass
# raise CargoOverload("Sorry, Cargo Over load!")


