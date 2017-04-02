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
  results = User.objects.filter(login__username=username)

  # 404 if username not in database
  if len(results) < 1:
    return HttpResponseNotFound('<h1>Page not found</h1>')
  elif len(results) > 1:
    print('PANIC: more than one matching user somehow')

  profile = results[0]

  # construct context
  friends = {}
  for friend in profile.friends.all():
    friends[friend.login.username] = str(friend.first_name) + ' ' + (friend.last_name)

  context = {'username': username, 
             'first_name': profile.first_name, 
             'last_name': profile.last_name,
             'profile_pic': profile.profile_pic,
             'location': profile.location,
             'about': profile.about,
             'reviews': profile.review_set.all(),
             'num_reviews': len(profile.review_set.all()),
             'media': profile.media_set.all(),
             'num_media': len(profile.media_set.all()),
             'friends': friends,
             'num_friends': len(friends),
             'bookmarks': profile.bookmark_set.all()}

  # Return the subpage that has been requested 
  if page == 'about':
    return render(request, 'website/profile-about.html', context)    
  elif page == 'bookmarks':
    return render(request, 'website/profile-bookmarks.html', context)
  elif page == 'photos':
    return render(request, 'website/profile-photos.html', context)
  elif page == 'reviews':
    return render(request, 'website/profile-reviews.html', context)
  elif page == 'friends':
    return render(request, 'website/profile-friends.html', context)

  # return 404 
  return HttpResponseNotFound('<h1>Page not found</h1>')

def destination(request, dest_id, page):
  results = Destination.objects.filter(id=dest_id)

  # 404 if dest_id not in database
  if len(results) < 1:
    return HttpResponseNotFound('<h1>Page not found</h1>')
  elif len(results) > 1:
    print('PANIC more than one result')

  dest = results[0]

  # construct context
  context = {'dest_id': dest_id,
             'name': dest.name,
             'media':  dest.media_set.all(),
             'reviews': dest.review_set.all()}

  if page == 'reviews':
    return render(request, 'website/destination-reviews.html', context)
  elif page == 'bookmarks':
    return render(request, 'website/destination-bookmark.html', context)
  elif page == 'friends':
    return render(request, 'website/destination-friends.html', context)
  elif page == 'photos':
    return render(request, 'website/destination-photos.html', context)
  elif page == 'creategroup':
    return render(request, 'website/destination-creategroup.html', context)
    
  return HttpResponseNotFound('<h1>Page not found</h1>') 

def planning(request, trip_id):
  return render(request, 'website/planning.html')

def search(request):
  return HttpResponse("Search Page")
