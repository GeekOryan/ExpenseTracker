import os
import json
from datetime import datetime

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
        print("/nMenu:")
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
            