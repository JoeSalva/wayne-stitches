from django.db import models
from decimal import Decimal
from django.conf import settings
from catalogue.models import Product
from .choices import NigerianStates

# Create your models here.

class Order(models.Model):
    class DELI_STATUS (models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        SHIPPED = 'SHIPPED', 'Shipped'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=DELI_STATUS.choices, default=DELI_STATUS.PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    end_total_price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    delivery_state = models.CharField(max_length=10, choices=NigerianStates.choices, blank=True)
    delivery_fee = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Order" 

    def get_total_price(self):
        return sum(item.total_price() for item in self.items.all()) # type:ignore
    
    def sum_qty(self):
        return sum(item.qty for item in self.items.all()) # type:ignore

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def total_price(self):
        return self.qty * self.price