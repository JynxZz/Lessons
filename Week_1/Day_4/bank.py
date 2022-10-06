class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    # TODO : withdraw 
    def withdraw(self, cash):
        if self.balance >= cash:
            self.balance -= cash
            return f"{self.name} has {self.balance}."
        else:
            raise ValueError#(f"{self.name} can't withdraw {cash}, he only has {self.balance}.")
    # TODO : check
    def check(self, who, cash): 
        if who.balance >= cash and who.checking_account:
            self.balance += cash
            who.balance -= cash
            return f"{self.name} has {self.balance} and {who.name} has {who.balance}."
        else:
            raise ValueError#(f"{who.name} doesn't have enough money.") 
    # TODO : add_cash
    def add_cash(self, cash):
        self.balance += cash
        return f"{self.name} has {self.balance}."