import csv
import os

FILE_NAME = "expense.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "amount", "description"])

Expenses = []

while True:
    print("\n-- Expense Tracker Menu --")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        Expenses.append({
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        })

        with open(FILE_NAME, mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("Expense Added Successfully!")

    elif choice == "2":
        print("\n--- Expenses from CSV ---")
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(
                    f"Date: {row[0]}, Category: {row[1]}, "
                    f"Amount: {row[2]}, Description: {row[3]}"
                )

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
