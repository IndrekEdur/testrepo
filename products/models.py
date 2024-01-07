from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
# New class for Project, which should have a name

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     client_project_manager = models.CharField(max_length=100)
#     client_project_manager_email = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name

class UserData( models.Model ) :
    def __str__( self ) :
       return self.user.username

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING )
    personal_id = models.CharField( max_length = 135, blank = True )
    phone = models.CharField( max_length = 135, blank = True )


class Project(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    project_number = models.IntegerField(unique=True)
    # project_manager = models.ForeignKey(User, related_name='manager', on_delete=models.DO_NOTHING, default=1)
    # project_client = models.ForeignKey(Client, related_name='client', on_delete=models.DO_NOTHING, default=1)
    dropbox_link = models.CharField(max_length=100)
    budget_dropbox_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
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

class Hours(models.Model):
    project = models.ForeignKey(Project, related_name='project',on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.DO_NOTHING, default=1)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING)
    inserted_at = models.DateTimeField(default=datetime.now, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def user_total_hours(self):
        return sum([item.hours.quantity for item in self.items.all()])

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)

class Remark(models.Model):
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)

class Invoice(models.Model):

    project_number = models.IntegerField(unique=False)
    project_name = models.CharField(max_length=50)
    account_number = models.IntegerField(unique=False)
    account_name = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    document_date = models.DateTimeField(default=datetime.now, blank=True)
    document_number = models.IntegerField(unique=False)
    accounting_entry = models.CharField(max_length=50)
    accounting_dimenson = models.CharField(max_length=50)
    invoice_description = models.CharField(max_length=50)
    amount = models.IntegerField(unique=False)
    unit = models.CharField(max_length=50)
    invoice_total = models.IntegerField(unique=False)

    def __str__(self):
        return self.name