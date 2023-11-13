class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, {self.id_number}, ${self.salary}"


class Manager(Employee):
    def __init__(self, name, id_number, salary, department):
        super().__init__(name, id_number, salary)
        self.department = department

    def get_department(self):
        return self.department


class Engineer(Employee):
    def __init__(self, name, id_number, salary, expertise):
        super().__init__(name, id_number, salary)
        self.expertise = expertise

    def get_expertise(self):
        return self.expertise


class Salesperson(Employee):
    def __init__(self, name, id_number, salary, experience):
        super().__init__(name, id_number, salary)
        self.experience = experience

    def get_experience(self):
        return self.experience
