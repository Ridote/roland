from django.conf.urls import url

from . import views
app_name='shoppinglist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addProduct, name='addProduct'),
    url(r'^about/$', views.aboutUs, name='aboutUs'),
    url(r'^remove/(?P<productId>[0-9]+)/$', views.removeProduct, name='removeProduct'),
]