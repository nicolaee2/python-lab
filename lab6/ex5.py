class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def __str__(self):
        return f"The {self.name} lives in {self.habitat}."


class Mammal(Animal):
    def __init__(self, name, habitat, feets):
        super().__init__(name, habitat)
        self.feets = feets

    def get_feets(self):
        return self.feets


class Bird(Animal):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def get_wing_span(self):
        return self.wing_span


class Fish(Animal):
    def __init__(self, name, habitat, location):
        super().__init__(name, habitat)
        self.location = location

    def get_location(self):
        return self.location
    