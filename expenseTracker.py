import os
from datetime import datetime
import csv

def main():
    print("Welcome to the Expense Tracker")
    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Exit")
        print("Please select an option (1, 2, or 3): ")
        choice = input()
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
# Defining a function to add a transaction
# This function will prompt the user for the necessary details of the transaction and then save it to a CSV file.
def add_transaction():
    print("Add a new transaction")
    date = input("Enter the date of the transaction (YYYY-MM-DD): ")
    amount = input("Enter the amount spent: ")
    category = input("Enter the category of the expense (e.g. Food, Transportation, Entertainment): ")
    description = input("Enter a brief description of the transaction: ")
    
    # User input validation will be added here to ensure that the date is in the correct format
    # and that the amount is a valid number. We will also handle any exceptions that may arise during this process.
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number for the amount spent.")
        return
    
    # If the input is valid, we will save the transaction to a CSV file.
    # We will check if the file exists, if not we will create it and add the headers.
    # Then we will append the new transaction to the file.
    
    file_exists = os.path.isfile('transactions.csv')
    # We will also implement error handling to ensure that any issues with file writing are gracefully handled.
    try:
        with open('transactions.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date', 'Amount', 'Category', 'Description'])
            writer.writerow([date, amount, category, description])
    except Exception as e:
        print(f"An error occurred while saving the transaction: {e}")
        return
    
# Defining a function to view the summary of transactions
# This function will read the transactions from the CSV file and calculate the total spent, total spent
# per category, and total spent per month. It will then display this information to the user.
def view_summary():
    print("Summary of Transactions")
    if not os.path.isfile('transactions.csv'):
        print("No transactions found. Please add a transaction first.")
        return
    total_spent = 0
    category_totals = {}
    month_totals = {}
    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) # This will skip the header line
            for row in reader:
                date, amount, category, description = row
                amount = float(amount)
                
                total_spent = total_spent + amount
                month = date[:7] # The exact month can be extracted from the date string (YYYY-MM)
                if category in category_totals:
                    category_totals[category] = category_totals[category] + amount
                else:
                    category_totals[category] = amount
                if month in month_totals:
                    month_totals[month] = month_totals[month] + amount
                else:
                    month_totals[month] = amount
    except Exception as e:
        print(f"An error has occurred while reading the transactions: {e}")
        return
    print(f"Total Spent: {total_spent}")
    print("Total Spent per Category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")
        
    print("Total Spent per Month:")    
    for month, total in month_totals.items():
        print(f"{month}: {total}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()