class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def display_balance(self):
        return round(self.balance, 2)


if __name__ == "__main__":
    acc = BankAccount("123", "Test User", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print("Final Balance:", acc.display_balance())
