
import csv
from datetime import datetime

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date!")
        return

    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount!")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def show_totals():
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        totals[category] = totals.get(category, 0) + amount

    print("\nTotal spending by category:")

    for category, total in totals.items():
        print(category, ":", total)


def save_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "category", "amount"]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved to CSV successfully!")


while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. Show Category Totals")
    print("3. Save to CSV")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_totals()
    elif choice == "3":
        save_csv()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
