'''
Banking Application
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
'''

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        


print("Welcome to the Bank")
print("How can we help you today?")
print("Select an option: \n 1. Create Account \n 2. Deposit Money \n 3. Withdraw Money \n 4. Check Balance \n 5. Exit")

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        account_number = input("Enter account number: ")
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))
        account = BankAccount(account_number, name, balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "4":
        account.check_balance()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        break


