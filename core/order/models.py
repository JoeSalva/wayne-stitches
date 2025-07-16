from django.db import models
from django.conf import settings
from catalogue.models import Product  

# Create your models here.

DELI_STATUS = [
    ('PENDING', 'Pending'),
    ('PROCESSING', 'Processing'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
]

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=DELI_STATUS, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def total_price(self):
        return self.qty * self.price