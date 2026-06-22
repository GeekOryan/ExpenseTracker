import os
import json
from datetime import datetime
import csv

# Let us start with the skeleton of the entire program. We will build the expense tracker step by step.
# Talk to me in comments first before proceeding to the code implementation.
# The expense tracker will have the following functionalities:
'''
It is a program that will be developed in Python and it will run in the Command Line Interface.

Data is stored in a csv file that can be accessed using even Microsoft Excel.

The user will be able to check their daily spend. It is a personal tool that can allow for the improvement of discipline in relation to unnecessary spending. So the details will be seen via a CSV file, showing total spent, per category and how much per month.
'''

'''
It will display a welcome message then follow through with a menu option, being add transaction, viewing summary and exit).

But there needs to be more fields inside add transaction, so that basically means create a CSV file, so once the transaction has been added the CSV file will be created and then that is when the user will enter other inputs (such as how much money they have made or have, how much they spent, what they spent it on, then that the program will automatically decide which category it falls under you know)

Summaries will be calculated for total in its entirety (Net) and then per category and per month. So three types of "totals"
Yes there will be error handling for both actually not just one. We need to gracefully handle as many unforeseen situations as possible.
'''

# Let's start by defining the main function that will run the program and display the menu options to the user.
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
        with open('transactions.csv', 'a') as file:
            if not file_exists:
                file.write('Date, Amount, Category, Description\n')
            file.write(f"{date}, {amount}, {category}, {description}\n")
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
            next(file) # This will skip the header line
            for line in file:
                date, amount, category, description = line.strip().split(', ')
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
    
    
# There is a bug for CSV writing with commas inside descriptions as it will break parsing.
# We need to use csv.writer and csv.DictReader to handle this properly. We will also need to update the code to use these modules for reading and writing to the CSV file. This will ensure that any commas in the description field are properly handled and do not break the parsing of the CSV file.


    