from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime
from .models import Product
from django.contrib.auth.models import User

def index(request):
	today = datetime.datetime.now().date()
	return render(request, "shoppinglist/index.html", {"today": today})

def viewProduct(request):
   me = User.objects.get(username='rido')
   products = Product.objects.filter(requester = me)
   return render(request, "shoppinglist/viewProducts.html", {"products": products})