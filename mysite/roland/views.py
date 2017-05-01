from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from datetime import datetime
from .models import *
from .forms import *
from .constants import INDEX_PUB_PER_PAGES
def index(request):
	publications = Publication.objects.filter(pub_date__lte = datetime.now()).order_by('-pub_date')[:INDEX_PUB_PER_PAGES]
	return render(request, "roland/index.html", {'publications': publications})
def newPublication(request):
	if request.method == "POST":
		form = PublicationForm(request.POST)
		if form.is_valid():
			publication = form.save(commit=False)
			publication.author = request.user
			publication.pub_date = datetime.strptime(request.POST['date'] + ' ' + request.POST['time'], '%Y-%m-%d %H:%M')
			publication.save()
			return redirect('roland:index')
	else:
		form = PublicationForm()
	return render(request, 'roland/newPublication.html', {"form": form})
def login(request):
	if(request.user.is_authenticated):
		return redirect('roland:index')
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user:
			if user.is_active:
				auth_login(request, user)
				return redirect('roland:index')
		else:
			error = "User/password does not match."
			return render(request, 'roland/login.html', {'error': error})
	else:
		return render(request, 'roland/login.html', {})
@login_required(login_url=LOGIN_URL)
def manual(request):
	manual = Manual.objects.filter(title='Roland')
	if(len(manual) > 0):
		manual = manual[0]
	categories = Category.objects.filter(manual=manual, superCategory__isnull=True)
	subcategories = []
	for category in categories:
		subcategoriesRaw = list(Category.objects.filter(manual=manual, superCategory=category))
		if subcategoriesRaw:
			subcategories.append(subcategoriesRaw)
		else:
			subcategories.append(None)
	return render(request, 'roland/manual.html', {'manual': manual, 'categories': categories, 'subcategories': subcategories})