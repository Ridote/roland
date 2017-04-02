from django.conf.urls import url

from . import views
app_name='shoppinglist'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^newProduct/$', views.NewProductView.as_view(), name='newProduct'),
    url(r'^addProduct/$', views.addProduct, name='addProduct'),
    url(r'^loginProcess/$', views.loginProcess, name='loginProcess'),
]