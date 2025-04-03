from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1, unique=True)  
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_quantity = models.PositiveIntegerField(null=True, blank=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

