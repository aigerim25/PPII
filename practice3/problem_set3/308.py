class Account:
    def __init__(self, balance,withdraw):
        self.balance = balance  
        self.withdraw = withdraw
    def newBalance(self):
        if self.balance > self.withdraw:
            return self.balance - self.withdraw
        elif self.balance == self.withdraw:
            return 0
        else:
            return "Insufficient Funds"     
balance,withdraw = map(int,input().split())
account = Account(balance,withdraw)
result = account.newBalance()
print(result) 




