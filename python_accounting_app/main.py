from python_accounting_app.data import DataStore
from python_accounting_app.operation import Operation

def format_amount(amount):
    return f"{amount:09.2f}"

def get_valid_amount(prompt):
    while True:
        print(prompt)
        value = input()
        value = value.replace(',', '.')
        try:
            amount = float(value)
            if amount < 0:
                print("Invalid amount. Please enter a positive value.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

def call_operations(op_type, ops):
    if op_type == "TOTAL":
        balance = ops.total()
        print(f"Current balance: {format_amount(balance)}")
    elif op_type == "CREDIT":
        amount = get_valid_amount("Enter credit amount:")
        old_balance = ops.total()
        new_balance = ops.credit(amount)
        if old_balance + amount > 999999.99:
            print("Warning: Maximum balance is 999999.99. The balance has been capped at this limit.")
        print(f"Amount credited. New balance: {format_amount(new_balance)}")
    elif op_type == "DEBIT":
        amount = get_valid_amount("Enter debit amount:")
        result = ops.debit(amount)
        if result == "Insufficient funds":
            print("Insufficient funds for this debit.")
        else:
            print(f"Amount debited. New balance: {format_amount(result)}")

def handle_choice(choice, ops):
    if choice == "1":
        call_operations("TOTAL", ops)
    elif choice == "2":
        call_operations("CREDIT", ops)
    elif choice == "3":
        call_operations("DEBIT", ops)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        return "EXIT"
    else:
        print("Invalid choice, please select 1-4.")

def menu_loop(ops):
    while True:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        print("Enter your choice (1-4):")
        choice = input()
        result = handle_choice(choice, ops)
        if result == "EXIT":
            break

def run():
    data_store = DataStore()
    ops = Operation(data_store)
    menu_loop(ops)

if __name__ == "__main__":
    run()
