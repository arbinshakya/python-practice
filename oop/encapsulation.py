# encapsulation
# note: Wrapping data and functions into a single unit(object)

class Account:
    
    def __init__ (self, balance, acc):
        self.balance = balance
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print(f"Total Balnce: {self.get_balance()}")


    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print(f"Total Balance: {self.get_balance()}")
        

    def get_balance(self):
        return self.balance


acc1 = Account(100000, 4343)
acc1.debit(500)
acc1.credit(200000)

# print(acc1.balance, acc1.acc)

        