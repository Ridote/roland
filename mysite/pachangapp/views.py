from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.db.models import Q
from datetime import datetime
from .models import *
from .forms import *
from .constants import LOGIN_URL
@login_required(login_url = LOGIN_URL)
def index(request):
	user = User.objects.filter(user=request.user).first()
	matches = Match.objects.filter(Q(team_home=user) | Q(team_visitant=user)).distinct()[:5]
	return render(request, "pachangapp/index.html", {'matches': matches})
@login_required(login_url = LOGIN_URL)
def stats(request, usernameID=False):
	if(not usernameID):
		query = request.user.username
	else:
		query = usernameID
	print(usernameID)
	print("\n\n\n")
	user = User.objects.filter(user__username=query).first()
	return render(request, "pachangapp/stats.html", {'profUser': user})
@login_required(login_url = LOGIN_URL)
def profile(request):
	user = User.objects.filter(user=request.user).first()
	if request.method == "POST":
		form = UserForm(user, request.POST)
		if form.is_valid():
			request.user.first_name = request.POST['first_name']
			request.user.last_name = request.POST['last_name']
			request.user.save()
			user.known_as = request.POST['known_as']
			user.save()
			return redirect('pachangapp:profile')
	else:
		form = UserForm(user)
	return render(request, 'pachangapp/profile.html', {"form": form, 'profUser': user})
def login(request):
	if(request.user.is_authenticated):
		return redirect('pachangapp:index')
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user:
			if user.is_active:
				auth_login(request, user)
				return redirect('pachangapp:index')
		else:
			error = "User/password does not match."
			return render(request, 'pachangapp/login.html', {'error': error})
	else:
		return render(request, 'pachangapp/login.html', {})