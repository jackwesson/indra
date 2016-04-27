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
from profilepage.views import index
from splash.forms import RegisterForm, LoginForm
from django.core.urlresolvers import reverse
from models import UserProfile


# superuser admin1
# admin1@example.com
# password11

# article that has useful stats on a competitor company
# https://www.entrepreneur.com/article/248011

def landing(request):
    
    return render(request, 'index.html')


# this is our login function
def login(request):
    
    email = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
        
        
        
        # The user model is a preset django model
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            request.session['mid'] = user.id
            request.session['loading'] = ''
            # request.session['mid'] can be used to identify the user later, request.session[landing] is used when loading other profile pages
            return HttpResponseRedirect ('/profilepage/')
    else:
        # logging sends the user to the profile page
        return render(request, 'index.html', {'errors': 'Invalid Login Information'})  
      
      
    # our register function, it returns errors in the events of bad inputs, will redirect to profile page  
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if len(username) > 50:
            return render(request, 'index.html', {'errors': 'Name is too long'})
        if len(username) == 0:
            return render(request, 'index.html', {'errors': 'Please enter a Username'})
        if len(email) > 50:
            return render(request, 'index.html', {'errors': 'E-mail is too long'})
        if len(password) > 50:
            return render(request, 'index.html', {'errors': 'Password is too long'})
        if len(password) == 0:
            return render(request, 'index.html', {'errors': 'Please enter a Password'})
        if User.objects.filter(email=email).exists():
            return render(request, 'index.html', {'errors': 'E-mail already in use'})
        if '@' in email:
            u = User.objects.create_user(username=username, email=email, password=password)
            u.save()
            if request.POST['usertype'] == 'venue':
                u.first_name = 'venue'
            else:
                u.first_name = 'entertainer'
            u.save() 
            request.session['mid'] = u.id
            request.session['loading'] = ''
            return HttpResponseRedirect ('/profilepage/')
        else:
            return render(request, 'index.html', {'errors': 'Enter a valid E-mail Address'})
