class Product: 
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def get_price(self):
        return self._price
    
    def info(self):
        return f'Name: {self._name}, Price: {self._price}'