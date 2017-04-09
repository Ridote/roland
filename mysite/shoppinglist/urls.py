from django.conf.urls import url

from . import views
app_name='shoppinglist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/', views.viewProduct, name='product'),
    url(r'^add/', views.addProduct, name='addProduct'),
]