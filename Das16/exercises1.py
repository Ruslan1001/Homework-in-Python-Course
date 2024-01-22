# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.

# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.

# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.


class BankAccount:
     def __init__(self,account_holder,balance=1000):
        self.account_holder=account_holder
        self.balance=balance
     def deposit(self,num):
          if num>0:
               self.balance+=num
               print( f"Deposit is {num}$")
          else:
              print("Deposit is not correct")
     def withdraw(self,number):
          if number>0 and number<=self.balance:
              self.balance-=number
              print(f"Withdraw is {number}$")
          else:
              print("Withdraw is not correct")
     def get_balance(self):
        return f"Balance of account_holder is {self.balance}$"  
account1=BankAccount(account_holder="Arshak")
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())
