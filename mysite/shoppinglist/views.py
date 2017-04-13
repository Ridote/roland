from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *

def index(request):
   me = User.objects.get(username='rido')
   products = Product.objects.filter(requester = me).order_by('predefinedProduct__category', 'predefinedProduct__name')
   return render(request, "shoppinglist/index.html", {"products": products})
def addProduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.requester = request.user
			#product.predefinedProduct = PredefinedProduct.objects.filter(name=product.predefinedProduct)
			product.save()
			return redirect('shoppinglist:addProduct')
	else:
		form = ProductForm()
	return render(request, 'shoppinglist/addProduct.html', {"form": form})
def adminCategory(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.save()
			return redirect('shoppinglist:adminCategory')
	else:
		form = CategoryForm()
	categories = Category.objects.all().order_by('name')
	return render(request, 'shoppinglist/adminCategory.html', {"form": form, "categories": categories})
def adminProductType(request):
	if request.method == "POST":
		form = ProductTypeForm(request.POST)
		if form.is_valid():
			productType = form.save(commit=False)
			productType.save()
			return redirect('shoppinglist:adminProductType')
	else:
		form = ProductTypeForm()
	products = PredefinedProduct.objects.all().order_by('name')
	return render(request, 'shoppinglist/adminProductType.html', {"form": form, "products": products})
def removeProduct(request, productId):
	Product.objects.filter(id = productId).delete()
	return redirect('shoppinglist:index')
def removeCategory(request, categoryId):
	Category.objects.filter(id = categoryId).delete()
	return redirect('shoppinglist:adminCategory')
def removeProductType(request, productTypeId):
	PredefinedProduct.objects.filter(id = productTypeId).delete()
	return redirect('shoppinglist:adminProductType')
def aboutUs(request):
	return render(request, 'shoppinglist/about.html', {})