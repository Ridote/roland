from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from .forms import ProductForm

def index(request):
	today = datetime.datetime.now().date()
	return render(request, "shoppinglist/index.html", {"today": today})

def viewProduct(request):
   me = User.objects.get(username='rido')
   products = Product.objects.filter(requester = me)
   return render(request, "shoppinglist/viewProducts.html", {"products": products})
def addProduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.requester = request.user
			product.save()
			return redirect('../../shoppinglist/products', pk=product.pk)
	else:
		form = ProductForm()
	return render(request, 'shoppinglist/addProduct.html', {"form": form})