from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def deliver(self, order):
        pass
    
class NovaPostaDelivery(DeliveryService):
    def deliver(self, order):
        return f'Заказ:{order},Доставка Новою Поштою оформлена'
    
class CourierDelivery(DeliveryService):
    def deliver(self, order):
        return f"Заказ:{order}, Кур’єрська доставка оформлена"