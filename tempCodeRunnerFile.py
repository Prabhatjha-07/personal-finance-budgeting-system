
except json.JSONDecodeError:
    print("Error decoding JSON from the file 'finance.json'.")
    exit()

if data["transactions"]: