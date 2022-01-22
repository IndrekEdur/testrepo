from django.db import models
from products.models import Product

class Check_out(models.Model):
    user_name = models.CharField(max_length=50)
    Date_of_submission = models.CharField(max_length=50)
    total_cost = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    order_items = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

