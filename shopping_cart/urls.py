"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success
)

app_name = 'shopping_cart'

urlpatterns = [

 path('list/', views.Shopping_cartListView.as_view(), name='shopping_cart_list'),
 path('delete/<int:pk>', views.Shopping_cart_itemDeleteView.as_view(), name='shopping_cart_itemDelete'),
 path('add/', views.Shopping_cart_itemAddView.as_view(), name='shopping_cart_itemAdd'),
 path('cart_add/', views.Shopping_cart_AddView.as_view(), name='shopping_cart_Add'),
 # From Just Django example
 url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
 url(r'^order-summary/$', order_details, name="order_summary"),
 url(r'^success/$', success, name='purchase_success'),
 url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
 url(r'^checkout/$', checkout, name='checkout'),
 url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
     name='update_records')
]
