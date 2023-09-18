''' Implement a class called bankaccount that represents a bank account .The class should have private.
attributes for account number, account holder name, and account balances.Include methods to
deposit money, withdraw money, and display the account balance. ensure that the account balance 
cannot be accessed directly from outside the class. write a program to create an instance of the
bank account class and test the deposit and withdrawal functionality.'''


class BankAccount:
  
  def __init__(self,account_number, account_holder_name, initial_balance=0.0):
   self.__account_number =   account_number
   self.__account_holder_name= account_holder_name
   self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0 :
       self.__account_balance  += amount
       # self.__account_balance= self.__account_balance + amount 
       print("Deposited  ${}.new balance:${}.".format(amount,
                                                 self.__account_balance))
    else:
        print("Invalid deposit amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
          self.__account_balance  -= amount
          #self.__account_balance= self.__account_balance -amount 
          print("withdraw  ${}. new balance: ${}".format (amount,
                                                 self.__account_balance))
    else:
      print(" Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
      print("Account balance for {}(account #{}):  ${}" .format(
                self.__account_holder_name, self.__account_number,
                    self.__account_balance))


# Create an instance of the BankAccount class
account = BankAccount(account_number="12345",
            account_holder_name="sivapriya",
                   initial_balance=15000.0)

# Test deposit and withdrawal functionality 
account.display_balance()
account.deposit(5000.0)
account.withdraw(2000.0)
account.withdraw(30000.0)
account.display_balance()