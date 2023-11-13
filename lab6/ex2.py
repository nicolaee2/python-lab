class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def calculate_interest(self):
        raise NotImplementedError("Not Implemented")


class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, balance=0, interest_rate=0.01):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate