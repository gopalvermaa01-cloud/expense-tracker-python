import json
expenses=[]
try:
    with open("expenses.json","r")as file:
        expenses=json.load(file)
except FileNotFoundError:
    expenses=[]
print("PERSONAL EXPENSE TRACKER")
print("Welcome!")
while True:
    print("\n--- MENU---")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Delete Expenses")
    print("4.Exit")
    choice=input("Enter your choice")
    if choice=="1":
        category=input("enter the expense category:").strip()
        if category=="":
            print("category cannot be empty")
            continue
        try:
            amount=float(input("Enter amount: "))
            if amount<=0:
                print("Amount must be greater than 0")
                continue
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue
        expense={
            "category":category,
            "Amount":amount
    }
        expenses.append(expense)
        with open("expenses.json","w")as file:
            json.dump(expenses, file, indent=4)
        print("Expense added successfully!")
    elif choice=="2":
        print("\n---EXPENSES---")
        if len(expense)==0:
            print("No expenses recorded")
        else:
            for i, expense in enumerate(expenses,start=1):
                print(f"{i}.{expense['category']}-{expense['Amount']:.2f}")
            total=sum(expense["Amount"] for expense in expenses)
            print(f"\nTotal Expense: {total:.2f}")
    elif choice=="3":
        if len(expenses)==0:
            print("No Expense to delete")
        else:
            print("\n---EXPENSE---")
            for i,expense in enumerate(expenses,start=1):
                print(f"{i}.{expense['category']}-{expense['Amount']:.2f}")
            number=int(input("Enter expense number to delete:"))
            if number>=1 and number<=len(expenses):
                deleted_expense = expenses.pop(number-1)
                print(f"{deleted_expense['category']}expense deleted successfully!")
            else:
                print("Invalid expense number!")
    elif choice=="4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! please try again")