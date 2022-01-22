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
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
# From Just Django example
from django.conf.urls import url
from accounts.views import my_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('products/', include('products.urls')),
    path('shopping_cart/', include('shopping_cart.urls')),
    path('check_out/', include('check_out.urls')),
    path('accounts/', include('accounts.urls')),
    url(r'^profile/$', my_profile, name='my_profile')
    # path('pdf/', include('pdf_convert.urls')),
    # path('emailsender/', include('send_email.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)