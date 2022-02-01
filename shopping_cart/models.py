from django.db import models
from products.models import Product
import datetime
from django.contrib.auth.models import User

class Shopping_cart(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.user_name)

class Shopping_cart_item(models.Model):
    shopping_cart = models.ForeignKey(Shopping_cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    product_quantity = models.DecimalField(default=1, max_digits=8, decimal_places=0)
    product_hours = models.DecimalField(default=1, max_digits=8, decimal_places=2)
    added_time = models.DateTimeField(default=datetime.datetime.now())
    item_cost = models.DecimalField(default=1, max_digits=8, decimal_places=2)

    def calc_total(self):
        amount = (self.product_hours * self.product_quantity)
        return amount

    def __str__(self):
        return self.shopping_cart_id

# From Just Django example
from accounts.models import Profile

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.hours for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)