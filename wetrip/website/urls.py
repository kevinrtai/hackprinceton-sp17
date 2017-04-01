from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'website/logout.html'}, name='logout'), 
    url(r'^profile', views.profile, name='profile'),
    url(r'^destination', views.destination, name='destination'),
    url(r'^tripplanner', views.planning, name='tripplanner'),
    url(r'^search', views.search , name='search')
]
