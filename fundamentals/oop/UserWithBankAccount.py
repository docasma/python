class BankAccount:
     accounts = []
     
     def __init__(self,balance,int_rate):
         self.balance= balance
         self.int_rate=int_rate
         BankAccount.accounts.append(self)

     def deposit(self,amount):
         self.balance += amount
         return self
     
     def withdrawl(self,amount):
         if self.balance >= amount:
            self.balance -= amount
         else:
            self.balance-=5
            print (f"Insufficient funds:charging a £ 5 fee")
         return self
          
     def display_account_info(self):
         return(f"Balance:{self.balance}")

     def yield_intrest(self):
         if self.balance > 0:
            self.balance += self.balance * self.int_rate
         return self

     @classmethod
     def print_all_info(cls):
         for account in cls.accounts:
             account.display_account_info()

class User:
   def __init__(self,name) -> None:
      self.name=name
      self.account = {
            "account_1":BankAccount(100000,0.5),
            "account_2" : BankAccount(50000,0.2)
      }


#display method
   def display_user_balance(self):
       print( f" User:{self.name} account_1 Balance:$ {self.account["account_1"].display_account_info()}")
       print( f" User:{self.name} account_2 Balance:$ {self.account["account_2"].display_account_info()}")

#transfer_money method
   def transfer_money(self,amount,user):
     self.amount-=amount
     user.amount+=amount
     self.display_user_balance()
     user.display_user_balance()
     return self

asma = User("Asma")
asma.account["account_1"].deposit(50000)
asma.display_user_balance()