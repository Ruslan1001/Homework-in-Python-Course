# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.
class BankAccount:
    def __init__(self,account_number,balance=1000):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit is {amount}")
            
        else:
            print("Deposit is not correct")

    def withdraw(self,amount):
        if amount>0:
            self.balance-=amount
            print(f"Withdraw is {amount}")

    def get_balance(self):
        return f"Balance is {self.balance}"
#account1=BankAccount(account_number="1235437846464")
#account1.deposit(250)
#print(account1.get_balance())

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance,interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate=interest_rate
    def deposit(self,amount,):
        if amount>0:
            self.balance+=amount
            self.balance+=amount/100*self.interest_rate
        print(f"Deposit is  {amount}")  
        print(f"Deposit interest_rate is {amount/100*self.interest_rate}")
savings_account1=SavingsAccount("1588964455311892",1500,25)
savings_account1.deposit(200)
print(savings_account1.get_balance())

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance,overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee=overdraft_fee
    def withdraw(self,amount):
        if  amount>0:
            self.balance-=amount 
        elif   self.balance<0 :
            self.balance-=self.overdraft_fee
            print(f"Withdraw is {amount}")
account2=CheckingAccount(415782100215478888888854,2000,200)  
account2.withdraw(2100)
print(account2.get_balance())
        

    
