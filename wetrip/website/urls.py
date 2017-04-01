from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^profile', views.profile, name='profil'),
    url(r'^destination', views.destination, name='destination'),
    url(r'^tripplanner', views.planning, name='tripplanner'),
    url(r'^search', views.search , name='search')
]
