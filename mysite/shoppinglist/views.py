from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Product, User

class LoginView(generic.ListView):
    template_name = 'shoppinglist/login.html'
    context_object_name = 'credentials'
    def get_queryset(self):
        return None
def loginProcess(request, username_str, password_str):
	user = get_object_or_404(User, username = username_str)
	print(user)
	
	'''
	return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	'''


class IndexView(generic.ListView):
    template_name = 'shoppinglist/index.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.order_by('-id')
class NewProductView(generic.ListView):
	template_name = 'shoppinglist/newProduct.html'
	context_object_name = 'userObject'
	def get_queryset(self):
		pk = 2
		return User.objects.filter(user_id=1)
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