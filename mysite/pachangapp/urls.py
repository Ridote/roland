from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name='pachangapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/pachangapp/'}, name='logout')
]