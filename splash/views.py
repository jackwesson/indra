#original 
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout
from .forms import RegisterForm
from django.http import HttpResponse

from models import UserProfile


# superuser admin1
# admin1@example.com
# password11


def landing(request):
    
    return render(request, 'index.html')


def login(request):
    
    email = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
        # password = request.POST.get('password', '')
        
        
        # The user model is a preset django model
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            request.session['mid'] = user.id
            # request.session['mid'] can be used to identify the user later
            return HttpResponseRedirect ('/profilepage/')
    else:
       
        return HttpResponse("Sorry your login information was wrong")   
    
def thanks(request):
    # this is the register function
    print ('please dont print this')
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    if email != "" and username != "" and password != "":
        u = User.objects.create_user(username=username, email=email, password=password)
        u.save()
        
        request.session['mid'] = u.id
        return HttpResponseRedirect ('/profilepage/')
        
    else:
        
        return render(request, 'index.html')

    
