class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def describe(self):
        return f"This is a Vehicle made by {self._make} with model {self._model}."


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def describe(self):
        return f"This is a Car made by {self._make} with model {self._model} and has {self.__num_doors} doors."


class Bike(Vehicle):
    _has_pedals = True

    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):
        return f"This is a Bike made by {self._make} with model {self._model}."
