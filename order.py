from delivery import DeliveryService

class Order:
    def __init__(self, user, cart, delivery_service):
        self.user = user
        self._cart = cart
        self._delivery_service = delivery_service
        
    def create(self):
        print(f'Your order create')
        
    def checkout(self):
        print(f'Доставка оформлена {self._delivery_service.deliver(self)}')
        
    def summary(self):
        return f'info: \nname: {self.user.get_name()}\nprice: {self._cart.total_price()}'