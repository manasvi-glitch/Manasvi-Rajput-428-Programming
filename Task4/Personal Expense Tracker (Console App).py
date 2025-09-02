# -------------------------------
# Personal Expense Tracker
# -------------------------------
from collections import defaultdict

def expense_tracker():
    # Dictionary to store expenses by category
    expenses = defaultdict(float)
    
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Total Spent")
        print("3. View Category Breakdown")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            category = input("Enter category (e.g. Food, Travel): ")
            amount = float(input("Enter amount: "))
            expenses[category] += amount
            print("Expense added!")
        
        elif choice == "2":
            total = sum(expenses.values())
            print(f"Total Spent: {total}")
        
        elif choice == "3":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nExpense Breakdown:")
                for category, amount in expenses.items():
                    print(f"- {category}: {amount}")
        
        elif choice == "4":
            print("Exiting Expense Tracker")
            break
        else:
            print("Invalid choice!")

# Run the Expense Tracker
expense_tracker()
