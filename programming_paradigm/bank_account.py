class BankAccount:
    def __init__(self, initial_balance=0):
        #initializing a new bank account
        self.account_balance = initial_balance

    def deposit(self, amount):
        #adding amount to the account balance
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.account_balance += amount

    def withdraw(self, amount):
        #deducting the specified amount if suffucuent funds are available
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        #prints the current balance
        print("Current Balance: ${self.account_balance}")