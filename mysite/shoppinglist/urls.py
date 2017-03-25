from django.conf.urls import url

from . import views
app_name='shoppinglist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addProduct/$', views.addProduct, name='newProduct'),
]