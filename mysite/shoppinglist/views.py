from django.shortcuts import render
from .models import Product, User
# Create your views here.

def index(request):
	products = Product.objects.order_by('-id')[:]
	context = {'products': products}
	return render(request, 'shoppinglist/index.html', context)

def addProduct(request):
	user = User.objects.order_by('-id')[1:]
	context = {'user': user}
	return render(request, 'shoppinglist/newProduct.html', context)