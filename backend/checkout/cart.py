from .models import Product
from collections import Counter
from decimal import Decimal


def calculate_total(cart_items):

    cart_counter = Counter(cart_items)
    # print(cart_counter)

    total_price = Decimal('0.00')  

    # print("total_price",total_price)

    # print("-------------------------------------------------------")

    for product_name, quantity in cart_counter.items():
        try:
            product = Product.objects.get(name=product_name)
            # print("product", product)

        except Product.DoesNotExist:

            continue

        quantity = int(quantity)

        if product.discount_quantity and quantity >= product.discount_quantity:

            discounted_sets = quantity // product.discount_quantity  
            # print("discounted_sets",discounted_sets)

            remaining_items = quantity % product.discount_quantity
            # print("remaining_items",remaining_items)

            total_price += (
                Decimal(discounted_sets) * product.discount_price +
                Decimal(remaining_items) * product.price
            )

            # print("total price ",total_price)
        else:
            total_price += Decimal(quantity) * product.price
            

    return total_price
