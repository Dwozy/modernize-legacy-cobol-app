class DataStore:
    def __init__(self):
        self._balance = 1000.00

    def read_balance(self):
        return self._balance

    def write_balance(self, new_balance):
        self._balance = new_balance
