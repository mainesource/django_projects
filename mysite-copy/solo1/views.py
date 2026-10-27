from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   return HttpResponse("Being right is highly overrated. Even a stopped clock is right twice a day.") 
