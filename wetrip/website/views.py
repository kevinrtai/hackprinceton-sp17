from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'website/index.html')

def login(request):
  return render(request, 'website/login.html')

def profile(request):
  return HttpResponse("Profile page")

def destination(request):
  return render(request, 'website/destination.html')

def planning(request):
  return HttpResponse("Planning Page")

def search(request):
  return HttpResponse("Search Page")
