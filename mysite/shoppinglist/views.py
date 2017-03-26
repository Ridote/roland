from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, User
# Create your views here.

def index(request):
	products = Product.objects.order_by('-id')[:]
	context = {'products': products}
	return render(request, 'shoppinglist/index.html', context)

def newProduct(request):
	user = get_object_or_404(User, pk=2)
	print(user.username)
	context = {'userObject': user}
	return render(request, 'shoppinglist/newProduct.html', context)
def addProduct(request):
	quantity = request.POST.get("quantity", "")
	name = request.POST.get("name", "")
	requester = request.POST.get("requesterId", "")
	user = get_object_or_404(User, pk=requester)
	context = {'addingProduct': True, 'userObject': user, 'quantity': quantity, 'name': name}
	
	return render(request, 'shoppinglist/newProduct.html', context)