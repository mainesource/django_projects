from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    num_sessions = request.session.get('num_sessions', 0) + 1
    request.session['num_sessions'] = num_sessions
    
    if num_sessions > 4:
        del(request.session['num_sessions'])
    
    response = HttpResponse('view count='+str(num_sessions))
    response.set_cookie('dj4e_cookie', '5ea97148', max_age=1000)
    
    return response
