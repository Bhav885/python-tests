# python_oop_example.py

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def get_balance(self):
        """Return the current balance"""
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Add interest to the account balance"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest Added: {interest}. New Balance: {self.balance}")
        return interest


# Interactive usage
if __name__ == "__main__":
    print("🏦 Welcome to the Bank System")

    acc_num = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    account = SavingsAccount(acc_num, name, balance)

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Add Interest")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif choice == "3":
            account.add_interest()

        elif choice == "4":
            print(f"Current Balance: {account.get_balance()}")

        elif choice == "5":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice! Please select between 1-5.")
