def add_budget(data):
    while True:
        category = input("Enter budget category: ").strip().lower()
        amount = float(input("Enter budget amount: ").strip())
        
        data["budgets"][category] = amount
        print("Budget added successfully.")
        
        choice = input("Do you want to add another budget? (y/n): ").strip().lower()
        if choice != "y":
            break   
    