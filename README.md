# Expense Tracker CSV

## About
A Python command-line tool for tracking personal income and expenses. 
Built for IT and Computer Science students, developers, and anyone who 
wants a simple way to build financial discipline without relying on a 
banking app or spreadsheet software. All data is stored in a CSV file 
that can be opened directly in Excel or Google Sheets.

## Features
- **Add Transaction** — record a transaction with a date, amount, 
  category and description
- **View Summary** — see total spent overall, broken down by category, 
  and broken down by month
- **CSV Storage** — all data saved to `transactions.csv`, readable in 
  any spreadsheet program
- **Input Validation** — invalid dates and non-numeric amounts are 
  caught and handled gracefully without crashing or corrupting data
- **Safe Comma Handling** — uses Python's built-in csv module so 
  descriptions containing commas don't break the file format

## How to Run

**Requirements:** Python 3 installed on your machine.

**Clone the repository:**
```bash
git clone https://github.com/GeekOryan/ExpenseTracker.git
```

**Navigate into the folder:**
```bash
cd ExpenseTracker
```

**Run the program:**
```bash
python expenseTracker.py
```

**When adding a transaction, enter the date in this format: YYYY-MM-DD**

## Tech Used
- Python 3
- `csv` module — reading and writing transaction data
- `datetime` module — validating date input
- `os` module — checking if the CSV file already exists
