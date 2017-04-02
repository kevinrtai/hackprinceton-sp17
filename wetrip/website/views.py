from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

from website.models import Login, User, Group, Media, Review, Destination, DestinationInfo, Trip

# Create your views here.
def index(request):
  return render(request, 'website/index.html')

def login(request):
  return render(request, 'website/login.html')

def profile(request, username, page):
  # 404 if username not in database
  if False:
    return HttpResponseNotFound('<h1>Page not found</h1>')

  # construct context
  context = {'username': username}

  # Return the subpage that has been requested 
  if page == 'about':
    return render(request, 'website/profile-about.html', context)    
  elif page == 'bookmarks':
    return render(request, 'website/profile-bookmarks.html', context)
  elif page == 'photos':
    return render(request, 'website/profile-photos.html', context)
  elif page == 'reviews':
    return render(request, 'website/profile-reviews.html', context)

  # return 404 
  return HttpResponseNotFound('<h1>Page not found</h1>')

def destination(request, dest_id, page):
  # 404 if dest_id not in database
  if False:
    return HttpResponseNotFound('<h1>Page not found</h1>')

  # construct context
  if page == 'reviews':
    return render(request, 'website/destination-reviews.html')
  elif page == 'bookmarks':
    return render(request, 'website/destination-bookmark.html')
  elif page == 'friends':
    return render(request, 'website/destination-friends.html')
  elif page == 'photos':
    return render(request, 'website/destination-photos.html')
  elif page == 'creategroup':
    return render(request, 'website/destination-creategroup.html')
    
  return HttpResponseNotFound('<h1>Page not found</h1>') 

def planning(request, trip_id):
  return render(request, 'website/planning.html')

def search(request):
  return HttpResponse("Search Page")
