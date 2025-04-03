from .models import Product
from collections import Counter

def calculate_total(cart_items):
    cart_counter = Counter(cart_items)
    print(cart_counter)
    total_price = 0

    for product_name, quantity in cart_counter.items():
        try:
            product = Product.objects.get(name=product_name)
            # print("first :", product)
        except Product.DoesNotExist:
            continue  

        if product.discount_quantity and quantity >= product.discount_quantity:
            # print("product.discount_quantity",product.discount_quantity)
            discounted_sets = quantity // product.discount_quantity
            # print("discounted_sets",discounted_sets)
            remaining_items = quantity % product.discount_quantity
            # print("remaining_items",remaining_items)
            total_price += discounted_sets * product.discount_price + remaining_items * product.price
            # print("total_price",total_price)
        else:
            total_price += quantity * product.price
            # print("total_price2",total_price)

    return total_price



class Cart:
    def __init__(self, cart_items):

        self.cart_items = cart_items
        self.cart_counter = Counter(cart_items)

    def get_product(self, product_name):

        try:
            return Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            return None

    def calculate_total(self):

        total_price = 0

        for product_name, quantity in self.cart_counter.items():
            product = self.get_product(product_name)
            if not product:
                continue  

            total_price += self.calculate_product_price(product, quantity)

        return total_price

    def calculate_product_price(self, product, quantity):

        if product.discount_quantity and quantity >= product.discount_quantity:
            discounted_sets = quantity // product.discount_quantity
            remaining_items = quantity % product.discount_quantity
            return discounted_sets * product.discount_price + remaining_items * product.price
        return quantity * product.price
