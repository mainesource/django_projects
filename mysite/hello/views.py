from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myview(request):
    sessions = request.session.get('sessions', 0) + 1
    request.session['sessions'] = sessions
    
    if sessions > 4 : del(request.session['sessions'])
    resp = HttpResponse('view count='+ str(sessions))
    resp.set_cookie('dj4e_cookie', '5fda550f', max_age=1000)
    return resp

