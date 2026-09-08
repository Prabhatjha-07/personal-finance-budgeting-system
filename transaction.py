def add_transaction(data):


    while True:

        if data["transactions"]:
            new_id = max(transaction["id"] for transaction in data["transactions"]) + 1
        else:
            new_id = 1

        transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
        amount = float(input("Enter transaction amount: "))
        category = input( "Enter transaction category: ").strip()
        description = input( "Enter transaction description: ").strip()
        date = input("Enter transaction date (YYYY-MM-DD): ").strip()

        transaction = {
            "id": new_id,
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        data["transactions"].append(transaction)

        print("Transaction added successfully.")

        choice = input(
            "Do you want to add another transaction? (y/n): "
        ).strip().lower()

        if choice != "y":
            break
    
def view_transactions(data):
    for transaction in data["transactions"]:
        print(f"ID: {transaction['id']}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: {transaction['amount']}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Date: {transaction['date']}")
        print("-" * 20)
    
def delete_transaction(data):
    while True:
        view_transactions(data)
        transaction_id = int(
            input("Enter the ID of the transaction to delete: ")
        )

        found = False

        for transaction in data["transactions"]:
            if transaction["id"] == transaction_id:
                found = True
                data["transactions"].remove(transaction)
                print("Transaction deleted successfully.")

                for index, transaction in enumerate(
                    data["transactions"], start=1
                ):
                    transaction["id"] = index

                return

        if not found:
            print("Transaction not found.")

        choice = input(
            "Do you want to try again? (y/n): ").strip().lower()

        if choice != "y":
            break

    print("Transaction not found.")