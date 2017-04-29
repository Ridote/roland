from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from datetime import datetime
from .models import *
#from .forms import *
#from .constants import INDEX_PUB_PER_PAGES
def index(request):
	matches = Match.objects.filter(team_home=request.user)[:5]
	return render(request, "pachangapp/index.html", {'matches': matches})
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