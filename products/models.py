from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
# New class for Project, which should have a name

class Project(models.Model):
    name = models.CharField(max_length=100)
    # method Project name (object) to see as string
    def __str__(self):
        return self.name
    is_active = models.BooleanField(default=True)

class Hours(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, default=2)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.DO_NOTHING, default=1)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    inserted_at = models.DateTimeField(default=datetime.now, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    # connect our product to Project, if we delete Project the product will be also deleted
    Project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, default=1, null=False)

    hours = models.DecimalField(max_digits=8, decimal_places=2)
    job_type = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=50)

    author = models.ForeignKey(User, related_name='author',on_delete=models.DO_NOTHING)
    performer = models.ForeignKey(User, related_name='performer', default=1,  on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='products', null=True, blank=True, default="products/box.jfif")
    availability = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
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