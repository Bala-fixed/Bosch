from datetime import datetime, timedelta

# Base class
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount} to {self.account_holder}'s account.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew {amount} from {self.account_holder}'s account.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.account_holder}: Balance = {self.balance:.2f}"


# Subclass: Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of {interest:.2f} applied to {self.account_holder}'s savings account.")


# Subclass: Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, overdraft_limit, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        print(f"Withdrew {amount} from {self.account_holder}'s current account (Overdraft used if needed).")


# Subclass: Fixed Deposit Account
class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, amount, interest_rate, lock_in_days):
        super().__init__(account_number, account_holder, amount)
        self.interest_rate = interest_rate
        self.lock_in_end_date = datetime.now() + timedelta(days=lock_in_days)

    def withdraw(self, amount):
        if datetime.now() < self.lock_in_end_date:
            raise Exception("Funds cannot be withdrawn before lock-in period ends.")
        super().withdraw(amount)

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of {interest:.2f} applied to {self.account_holder}'s fixed deposit account.")


# Bank class to manage multiple accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"Account for {account.account_holder} added successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer_funds(self, from_account_num, to_account_num, amount):
        from_acc = self.get_account(from_account_num)
        to_acc = self.get_account(to_account_num)

        if not from_acc or not to_acc:
            raise ValueError("Invalid account number(s) provided.")

        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Transferred {amount} from {from_acc.account_holder} to {to_acc.account_holder}.")


# Test Program
if __name__ == "__main__":
    bank = Bank()

    # Create accounts
    savings = SavingsAccount("S1001", "Alice", interest_rate=5.0, balance=1000.0)
    current = CurrentAccount("C1001", "Bob", overdraft_limit=500.0, balance=500.0)
    fixed_deposit = FixedDepositAccount("FD1001", "Charlie", amount=2000.0, interest_rate=6.5, lock_in_days=30)

    # Add to bank
    bank.add_account(savings)
    bank.add_account(current)
    bank.add_account(fixed_deposit)

    # Perform actions
    print("\n--- Savings Account ---")
    savings.deposit(200)
    savings.withdraw(150)
    savings.apply_interest()
    print(savings)

    print("\n--- Current Account ---")
    current.withdraw(900)  # Uses overdraft
    current.deposit(400)
    print(current)

    print("\n--- Fixed Deposit Account ---")
    try:
        fixed_deposit.withdraw(500)  # Should raise error due to lock-in period
    except Exception as e:
        print(f"Error: {e}")
    fixed_deposit.apply_interest()
    print(fixed_deposit)

    print("\n--- Fund Transfer ---")
    try:
        bank.transfer_funds("S1001", "C1001", 300)
    except Exception as e:
        print(f"Transfer failed: {e}")
    print(savings)
    print(current)


