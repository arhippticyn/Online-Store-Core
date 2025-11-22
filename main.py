from user import User
from cart import Cart
from product import Product
from discount_product import DiscountProduct
from delivery import NovaPostaDelivery
from order import Order

user = User("Archip", "archip@example.com")

cart = Cart()
cart.add_product(Product("Laptop", 30000))
cart.add_product(DiscountProduct("Headphones", 2000, 15))

delivery = NovaPostaDelivery()

order = Order(user, cart, delivery)
order.create()
order.checkout()
print(order.summary())

