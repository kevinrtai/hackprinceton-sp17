from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'website/logout.html'}, name='logout'), 
    url(r'^profile/(?P<username>[a-zA-Z]+)/(?P<page>[a-zA-Z]+)/', views.profile, name='profile'),
    url(r'^destination/(?P<dest_id>[0-9]+)/(?P<page>[a-zA-z]+)/', views.destination, name='destination'),
    url(r'^tripplanner/(?P<trip_id>[0-9]+)/', views.planning, name='tripplanner'),
    url(r'^search/', views.search , name='search')
]
