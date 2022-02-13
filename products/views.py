from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
import json

from . models import Product, Project, Comment, Hours
from . forms import ProductForm, CommentForm, HoursForm

import smtplib
from email.message import EmailMessage

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

@login_required(login_url='accounts/login.html')
def ShowAllProducts(request):

    project = request.GET.get('project')

    if project == None:
        products = Product.objects.order_by('created_at').filter(is_completed=False)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 8)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Product.objects.order_by('created_at').filter(Project__name=project, is_completed=False)

    projects = Project.objects.all()

    context = {
        'products': products,
        'projects': projects
     }

    return render(request, 'products/showProducts.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    productId = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    # create an order
    # create cart in session
    cartItems = request.session.get('cartItems', 0)
    request.session['cartItems'] = cartItems + 1

    return JsonResponse({'message': 'Item was added'})


class ProductCreateView(CreateView):
    model = Product
    Product.objects.order_by().filter()
    template_name = 'products/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')

@login_required(login_url='showProducts')
def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm()
    context = {
        "form": form
     }
    return render(request, 'products/addProduct.html', context)

@login_required(login_url='showProducts')
def addHours(request, pk):

    product = Product.objects.get(id=pk)
    project = product.Project
    form = HoursForm(instance=project)
    if request.method == 'POST':
        form = HoursForm(request.POST, instance=project)
        if form.is_valid():
            owner = request.user.id
            quantity = form.cleaned_data['quantity']
            date = form.cleaned_data['date']
            c = Hours(project=project, date=date, owner=request.user, quantity=quantity, inserted_at=datetime.now())
            c.save()
            return redirect('showProducts')
    else:
        form = HoursForm()

    return render(request, 'products/addHours.html', {'form': form })



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

@login_required(login_url='showProducts')
def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)

    num_comments = Comment.objects.filter(product=eachProduct).count()

    context = {
        'eachProduct': eachProduct,
        'num_comments': num_comments,
     }

    return render(request, 'products/productDetail.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product_list')

@login_required(login_url='showProducts')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            sendNotification(request, pk, product.author.email, " : has been updated! ")
            return redirect('showProducts')

    context = {
        "form": form,
    }

    return render(request, 'products/updateProduct.html', context)

@login_required(login_url='sendNotification')
def sendNotification(request, pk, email, content):
    product = Product.objects.get(id=pk)

    msg = EmailMessage()
    msg.set_content( product.Project.name + " : " + product.name + "  >>>  " + content + "  Here is the link for details: http://indreke.pythonanywhere.com/products/product/"+str(pk)+"/" + "   Description: " + product.description)
    msg['subject'] = product.Project.name + " : " + product.name
    msg['to'] = email

    user = "erlin.virtuaalne.assistent@gmail.com"
    msg['from'] = user
    password = "ipjykvcufysqigsc"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

    return redirect('showProducts')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    sendNotification(request, pk, product.author.email, " : has been deleted! ")
    product.delete()
    return redirect('showProducts')


@login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(hours__icontains=query)
            return render(request, 'products/searchbar.html', {'products': products})
        else:
            print("No information to show")
            return render(request, 'products/searchbar.html', {})


def add_comment(request, pk):
    eachProduct = Product.objects.get(id=pk)

    form = CommentForm(instance=eachProduct)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            sendNotification(request, pk, product.author.email, " : has been commented! ")
            return redirect('showProducts')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'products/add_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    return redirect(reverse('product', args=[product_id]))