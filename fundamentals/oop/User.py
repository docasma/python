class User:
   def __init__(self,name) -> None:
      self.name=name
      self.amount=0

#deposit method:
   def deposit(self,amount):
      self.amount+=amount
      return self

#withdrawl method:
   def withdrawl( self,amount):
     self.amount-= amount
     return self

#display method
   def display_user_balance(self):
       print( f" User:{self.name} Balance:$ {self.amount}")

#transfer_money method
   def transfer_money(self,amount,user):
     self.amount-=amount
     user.amount+=amount
     self.display_user_balance()
     user.display_user_balance()
     return self



#3 instances of user class 
user1= User("Amin")
user2= User ("Emna")
user3 = User("Alya")

#
user1.deposit(100).deposit(100).deposit(100).withdrawl(50).display_user_balance()
user2.deposit(100).deposit(100).withdrawl(50).withdrawl(50).display_user_balance()
user3.deposit(100).withdrawl(50).withdrawl(50).withdrawl(50)

user1.transfer_money(300,user3)
