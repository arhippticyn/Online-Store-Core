class Cart:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
        
    def total_price(self):
        total = 0
        for p in self.products:
            total += p.get_price()
        return total
    
    def count(self):
        return len(self.products)