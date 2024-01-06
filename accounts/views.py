from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCreationForm
from django.shortcuts import render, redirect
import pdb

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {"form": form}
    return render(request, "accounts/register.html", context)


# Create your views here.
def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            request.session['username']=user.username
            login(request, user)
            return redirect('/products/list/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):

    if request.method == "GET":
        logout(request)
        return redirect("/accounts/login/")
    return render(request, "accounts/logout.html", {})


# From Just Django example
from shopping_cart.models import Order
from .models import Profile

def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)