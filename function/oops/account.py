class Account:
    def __init__(self , holder_name, account, balance):
          self.holder=holder_name
          self.account=account
          self.balance=balance

    def debit(self, amount):
         self.balance-=amount
         print(self.holder, "debited money" ,amount ,"total balance", self.balance)

    
    def credit(self, amount):
         self.balance+=amount
         print(self.holder, "credited money" ,amount ,"total balance", self.balance)   

acc=Account( "kajal", 1234, 20000 ) 
acc.debit(1000)
acc.credit(500)          


             