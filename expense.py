# Expense Tracker

# Initialize an empty dictionary to store expenses
expense_data = {}

def add_expense():
    """
    Allows users to input their daily expenses.
    """
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the expense category: ")

    # Create an expense entry
    expense_entry = {
        "date": date,
        "amount": amount,
        "description": description,
        "category": category,
    }

    # Add the entry to the expense data
    expense_data.setdefault(date, []).append(expense_entry)
    print("Expense added successfully!")

def view_summaries():
    """
    Displays summaries of monthly expenses and category-wise expenditure.
    """
    # Calculate total expenses for each month
    monthly_totals = {}
    for date, expenses in expense_data.items():
        month = date[:7]  # Extract the year-month part
        total_amount = sum(entry["amount"] for entry in expenses)
        monthly_totals.setdefault(month, 0)
        monthly_totals[month] += total_amount

    print("\nMonthly Expense Summaries:")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")

    # Generate category-wise summaries
    categories = set(entry["category"] for expenses in expense_data.values() for entry in expenses)
    print("\nCategory-wise Expenditure:")
    for category in categories:
        category_total = sum(entry["amount"] for expenses in expense_data.values() for entry in expenses if entry["category"] == category)
        print(f"{category}: ${category_total:.2f}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summaries")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summaries()
        elif choice == "3":
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
