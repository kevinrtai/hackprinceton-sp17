from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'website/index.html')

def login(request):
  return render(request, 'website/login.html')

def profile(request):
  return render(request, 'website/profile-about.html')

def destination(request):
  return render(request, 'website/destination-reviews.html')

def planning(request):
  return render(request, 'website/planning.html')

def search(request):
  return HttpResponse("Search Page")
