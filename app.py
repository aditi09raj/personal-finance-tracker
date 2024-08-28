import sys
from database import setup, add_entry, view_all, delete_entry, check_balance

def display_menu():
    print("\n" + "="*40)
    print("    Personal Finance Tracker")
    print("="*40)
    print("1. Add New Transaction")
    print("2. View All Transactions")
    print("3. Check Balance")
    print("4. Delete a Transaction")
    print("5. Exit")
    print("="*40)

def get_transaction_type():
    while True:
        trans_type = input("Type (i for Income / e for Expense): ").lower()
        if trans_type == 'i':
            return "Income"
        elif trans_type == 'e':
            return "Expense"
        else:
            print("Invalid input. Please enter 'i' for Income or 'e' for Expense.")

def add_transaction():
    date = input("\nEnter Date (DD-MM-YY): ")
    trans_type = get_transaction_type()
    category = input("Category (e.g., Food, Rent, Salary): ")
    amount = float(input("Amount (₹): "))
    description = input("Description (optional): ")

    add_entry(date, trans_type, category, amount, description)
    print("Transaction added successfully!")

def view_transactions():
    records = view_all()
    if not records:
        print("No transactions found.")
    else:
        print("\n" + "-"*70)
        print(f"{'ID':<5} {'Date':<10} {'Type':<10} {'Category':<15} {'Amount (₹)':<12} {'Description'}")
        print("-"*70)
        for record in records:
            print(f"{record[0]:<5} {record[1]:<10} {record[2]:<10} {record[3]:<15} {record[4]:<12.2f} {record[5]}")
        print("-"*70)

def delete_transaction():
    entry_id = int(input("\nEnter the ID of the transaction to delete: "))
    delete_entry(entry_id)
    print("Transaction deleted successfully!")

def check_current_balance():
    balance = check_balance()
    print(f"\nCurrent Balance: ₹{balance:.2f}")

def main():
    setup()
    
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            check_current_balance()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            print("Exiting... Have a great day!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
