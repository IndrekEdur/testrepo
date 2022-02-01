from django.db import models
from datetime import datetime

# Create your models here.

# New class for Project, which should have a name

class Project(models.Model):
    name = models.CharField(max_length=100)
    # method Project name (object) to see as string
    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    # connect our product to Project, if we delete Project the product will be also deleted
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, default=True, null=False)

    hours = models.DecimalField(max_digits=8, decimal_places=2)
    product_type = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    availability = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)