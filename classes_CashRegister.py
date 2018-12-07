class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
    def getTotal(self):
        return self._totalPrice
    def getCount(self):
        return self._itemCount
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    def getPounds(self):
        self._totalPrice=int(self._totalPrice)

    def giveChange(self,payment):
        if payment<self._totalPrice:
            return "Money insufficient"
        else:
            return "%.2f"%(payment-self._totalPrice)

register1=CashRegister()
register1.addItem(12.4)
register1.addItem(3.25)
print(register1.giveChange(15.60))
print(register1.giveChange(15.65))
