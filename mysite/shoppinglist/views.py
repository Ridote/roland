from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from .forms import ProductForm

def index(request):
   me = User.objects.get(username='rido')
   products = Product.objects.filter(requester = me)
   return render(request, "shoppinglist/index.html", {"products": products})
def addProduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.requester = request.user
			product.save()
			return redirect('shoppinglist:index')
	else:
		form = ProductForm()
	return render(request, 'shoppinglist/addProduct.html', {"form": form})
def removeProduct(request, productId):
	product = Product.objects.filter(id = productId).delete()
	return redirect('shoppinglist:index')
def aboutUs(request):
	return render(request, 'shoppinglist/about.html', {})