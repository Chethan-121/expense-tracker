# Expense Tracker Project - Updated Version

import csv
import os
from datetime import datetime

FILE_NAME = "expense.csv"

# Create CSV file with header if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "amount", "description"])

# Load existing expenses from CSV into memory
def load_expenses():
    expenses = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append({
                "date": datetime.strptime(row["date"], "%d-%m-%Y"),
                "category": row["category"],
                "amount": float(row["amount"]),
                "description": row["description"]
            })
    return expenses

Expenses = load_expenses()

# Save all expenses back to CSV
def save_expenses():
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "amount", "description"])
        for exp in Expenses:
            writer.writerow([
                exp["date"].strftime("%d-%m-%Y"),
                exp["category"],
                exp["amount"],
                exp["description"]
            ])

# Main program loop
while True:
    print("\n-- Expense Tracker Menu --")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Date input with validation
        while True:
            date_input = input("Enter date (DD-MM-YYYY): ")
            try:
                date = datetime.strptime(date_input, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date format! Please use DD-MM-YYYY")

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        Expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })

        save_expenses()
        print("Expense Added Successfully!")

    elif choice == "2":
        if not Expenses:
            print("No expenses found.")
            continue

        # Sort by date
        Expenses.sort(key=lambda x: x["date"])
        print("\n--- All Expenses ---")
        for idx, exp in enumerate(Expenses, start=1):
            print(
                f"{idx}. Date: {exp['date'].strftime('%d-%m-%Y')}, "
                f"Category: {exp['category']}, "
                f"Amount: {exp['amount']}, "
                f"Description: {exp['description']}"
            )

    elif choice == "3":
        if not Expenses:
            print("No expenses to delete.")
            continue

        # Display expenses with index
        print("\n--- Expenses ---")
        for idx, exp in enumerate(Expenses, start=1):
            print(
                f"{idx}. Date: {exp['date'].strftime('%d-%m-%Y')}, "
                f"Category: {exp['category']}, "
                f"Amount: {exp['amount']}, "
                f"Description: {exp['description']}"
            )

        del_index = int(input("Enter the number of the expense to delete: "))
        if 1 <= del_index <= len(Expenses):
            removed = Expenses.pop(del_index - 1)
            save_expenses()
            print(f"Deleted expense: {removed['description']} ({removed['amount']})")
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
