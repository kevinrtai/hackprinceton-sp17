from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
  template = loader.get_template('website/index.html')
  context = {}
  return HttpResponse(template.render(context, request))

def login(request):
  return HttpResponse("Login page") 

def profile(request):
  return HttpResponse("Profile page")

def destination(request):
  return HttpResponse("Destination page")

def planning(request):
  return HttpResponse("Planning Page")

def search(request):
  return HttpResponse("Search Page")
