import json

from transaction import add_transaction, delete_transaction, view_transactions

try:
    with open("data/finance.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = {
        "transactions": [],
        "budgets": {}
    }

except json.JSONDecodeError:
    print("Error decoding JSON...")
    data = {
        "transactions": [],
        "budgets": {}
    }


def menu():
    print("\n===== Finance Tracker =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Delete Transaction")
    print("4. View Budget")
    print("5. Exit")


while True:

    menu()

    choice = input("Enter your choice: ").strip()

    match choice:

        case "1":
            add_transaction(data)

            with open("data/finance.json", "w") as file:
                json.dump(data, file, indent=4)

        case "2":
            view_transactions(data)

        case "3":
            delete_transaction(data)
            
            with open("data/finance.json", "w") as file:
                json.dump(data, file, indent=4)

        case "4":
            print("View Budget")

        case "5":
            print("Exit")
            break

        case _:
            print("Invalid choice")
    
    
            
