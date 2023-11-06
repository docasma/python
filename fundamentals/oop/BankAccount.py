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
         print(f"Balance:{self.balance}")
         return self

     def yield_intrest(self):
         if self.balance > 0:
            self.balance += self.balance * self.int_rate
         return self

     @classmethod
     def print_all_info(cls):
         for account in cls.accounts:
             account.display_account_info()

account_1=BankAccount(100000,0.5)
account_2 = BankAccount(50000,0.2)

account_1.deposit(500).deposit(600).deposit(700).withdrawl(100).yield_intrest().display_account_info()
account_2.deposit(200).deposit(500).withdrawl(100).withdrawl(50).withdrawl(70).withdrawl(80).yield_intrest().display_account_info()

BankAccount.print_all_info()