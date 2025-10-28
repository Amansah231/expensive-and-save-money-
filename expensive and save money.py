import json
from datetime import datetime

# File to store transactions
FILE_NAME = "expenses.json"

# Load transactions from file
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save transactions to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add income or expense
def add_transaction(transactions, trans_type):
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    desc = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transaction = {
        "type": trans_type,
        "amount": amount,
        "description": desc,
        "date": date
    }
    
    transactions.append(transaction)
    save_data(transactions)
    print(f"{trans_type.capitalize()} recorded successfully!\n")

# View transactions and balance
def view_balance(transactions):
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expense
    
    print("\n=== Transaction History ===")
    if transactions:
        for t in transactions:
            print(f"{t['date']} | {t['type'].capitalize()} | {t['amount']} | {t['description']}")
    else:
        print("No transactions yet.")
    
    print("\n--- Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Current Balance: {balance}\n")

# Main program
def main():
    transactions = load_data()
    
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance & History")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_transaction(transactions, "income")
        elif choice == "2":
            add_transaction(transactions, "expense")
        elif choice == "3":
            view_balance(transactions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

