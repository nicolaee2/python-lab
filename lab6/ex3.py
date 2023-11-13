class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'


class Car(Vehicle):
    def __init__(self, make, model, year, mpl):
        super().__init__(make, model, year)
        self.mpl = mpl

    def calculate_mileage(self, liters):
        return liters * self.mpl


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mpl):
        super().__init__(make, model, year)
        self.mpl = mpl

    def calculate_mileage(self, liters):
        return liters * self.mpl


class Truck(Vehicle):
    def __init__(self, make, model, year, tow_capacity):
        super().__init__(make, model, year)
        self.tow_capacity = tow_capacity

    def calculate_tow_capacity(self):
        return self.tow_capacity