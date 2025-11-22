from product import Product

class DiscountProduct(Product):
    def __init__(self, name, price, percent):
        super().__init__(name, price)
        self._percent = percent
        
    def get_price(self):
        return self._price - (1 + self._percent / 100)