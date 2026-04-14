#create a class called Order which stores item & its price.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, od2):
        return self.price > od2.price
    
    def compare(self, od1, od2):
        if od1.price > od2.price:
            return False
        else:
            return True
    
    


od1 = Order('momo', 100)
od2 = Order('pizza', 200)

print(od1 > od2)

print(od1.compare(od1, od2))
