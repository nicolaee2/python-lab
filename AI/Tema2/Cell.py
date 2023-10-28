class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.is_special = False
        self.domain = []

    def set_domain(self, domain):
        self.domain = domain

    def set_value(self, value):
        self.value = value

    def set_special(self, is_special):
        self.is_special = is_special

    def get_value(self):
        return self.value

    def get_domain(self):
        return self.domain

    def get_special(self):
        return self.is_special

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return str(self.value)