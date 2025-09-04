from python_accounting_app.data import DataStore

MAX_BALANCE = 999999.99

class Operation:
    def __init__(self, data_store: DataStore):
        self.data_store = data_store

    def total(self):
        return self.data_store.read_balance()

    def credit(self, amount):
        balance = self.data_store.read_balance()
        new_balance = balance + amount
        if new_balance > MAX_BALANCE:
            new_balance = MAX_BALANCE
        self.data_store.write_balance(new_balance)
        return new_balance

    def debit(self, amount):
        balance = self.data_store.read_balance()
        if amount > balance:
            return "Insufficient funds"
        new_balance = balance - amount
        self.data_store.write_balance(new_balance)
        return new_balance
