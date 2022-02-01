from django.shortcuts import render

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

from . models import Product, Project, Comment
from . forms import ProductForm, CommentForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

@login_required(login_url='accounts/login')
def ShowAllProducts(request):

    project = request.GET.get('project')

    if project == None:
        products = Product.objects.order_by('-hours').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 8)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Product.objects.filter(Project__name=project)

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
    form = ProductForm()

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
            return redirect('showProducts')

    context = {
        "form": form
    }

    return render(request, 'products/updateProduct.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
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
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
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