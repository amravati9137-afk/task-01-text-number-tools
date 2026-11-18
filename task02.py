
# Task 02 - Expense Tracker

import csv
from datetime import datetime

# Function 1: Validate date
def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date! Please enter YYYY-MM-DD.")


# Function 2: Validate amount
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


# Function 3: Add expenses
def add_expenses():
    expenses = []

    while True:
        print("\nEnter Expense Details")

        date = get_valid_date()
        category = input("Enter category: ").strip()

        while not category:
            print("Category cannot be empty.")
            category = input("Enter category: ").strip()

        amount = get_valid_amount()

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        choice = input("Add another expense? (yes/no): ").lower()

        if choice != "yes":
            break

    return expenses


# Function 4: Calculate category totals
def calculate_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals


# Function 5: Save expenses to CSV
def save_to_csv(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "category", "amount"]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("\nExpenses saved to expenses.csv")


# Main program
print("===== EXPENSE TRACKER =====")

expenses = add_expenses()

print("\n----- Category Wise Spending -----")

totals = calculate_totals(expenses)

for category, total in totals.items():
    print(category, ":", total)

save_to_csv(expenses)

print("\nThank you for using Expense Tracker!")
