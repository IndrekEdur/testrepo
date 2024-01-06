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
from .views import ShowAllProducts
# app_name = 'products'

urlpatterns = [
 path('list/', views.ProductListView.as_view(), name='product_list'),
 path('create/', views.ProductCreateView.as_view(), name='product_create'),
 path('create_project/', views.ProjectCreateView.as_view(), name='project_create'),
 path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
 path('project_general/<int:pk>', views.ProjectGeneralView, name='project_general'),
 path('project_detail/<int:pk>', views.ProjectDetailView, name='project_detail'),
 path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
 path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
 path('hours_update/<int:pk>', views.HoursUpdateView.as_view(), name='hours_update'),
 path('delete_hours/<int:pk>', views.HoursDeleteView.as_view(), name='hours_delete'),
 path('update_item/', views.updateItem, name="update_item"),
 path('', views.ShowAllProducts, name='showProducts'),
 path('project_list/', views.ShowAllProjects, name='showProjects'),
 path('users_list/', views.ShowAllUsers, name='showUsers'),
 path('product/<int:pk>/', views.productDetail, name='product'),
 path('addProduct/', views.addProduct, name='addProduct'),
 path('addHours/<int:pk>/', views.addHours, name='addHours'),
 path('addHoursGeneral/', views.addGeneralHours, name='addGeneralHours'),
 path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
 path('updateProject/<int:pk>/', views.updateProject, name='updateProject'),
 path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
 path('sendNotification/<int:pk>,<str:email>, <str:content>/', views.sendNotification, name='sendNotification'),
 path('search/', views.searchBar, name='search'),
 path('product/<int:pk>/add-comment', views.add_comment, name='add-comment'),
 path('product/<int:pk>/delete-comment', views.delete_comment, name='delete-comment'),

 path('userHours/<int:pk>', views.WorkingHoursListView, name='working-hours'),
 path('userHoursByProject/<int:pk>', views.WorkingHoursListByProjectsView, name='working-hours-by-projects'),
 path('userHoursList/<int:pk>', views.UserHoursListView, name='hours_list_of_user'),

 url(r'^', views.ShowAllProducts, name='product-list'),
]
