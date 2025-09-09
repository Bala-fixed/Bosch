class BankAccount:
    def _init_(self,account_number,account_holder,balance=0.0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amnt):
        if amnt<0:
            print("Enter valid amount")
        else:
            self.balance+=amnt
        print("Deposited {amount} to {account_holder}'s account")

    def withdraw(self,amnt):
        if amnt>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amnt
        print("Withdrew {amount} from {account_holder}'s account. Balance remaining: {balance}")

    def get_balance(self):
        print("Balance available: {self.balance}")

    def _str_(self):
        print(f"Account[{self.account_number}] - {self.account_holder}: Balance = {self.balance:.2f}")

class SavingsAccount(BankAccount):
    def _init_(self,account_number,account_holder,interest_rate,balance=0.0):
        super().init(self,account_number,account_holder,balance)
        self.interest_rate=interest_rate

    def apply_interest(self):
        interest= (self.balance*(rate/100))
        self.balance+=interest
        print("Interest of {interest} has been added. Balance:{balance}")
    
class CurrentAccount(BankAccount):
    def _init_(self,account_number, account_holder,overdraft_limit,balance=0.0):
        super()._init(sellf,account_number,account_holder,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self, amnt):
        if amnt<0:
            print("Withdraw amount must be positive")
        elif amnt>self.overdraft_limit+self.balance:
            print("Amount exceeds overdraft limit")
        else:
            self.balance= (self.balance+self.overdraft_limit)-amnt
            print("Withdrew {amnt} from {self.account_holder}'s account. Withdraw limit:{self.balance}")

class FixedAccount(BankAccount):
    def _init_(self,account_number,account_holder,lockinperiod,balance=0.0):
        super()._init_(self,account_number,account_holder,balance)
        self.lockinperiod=lockinperiod

    def lock(self,lockin):
        if

        

    
    


    