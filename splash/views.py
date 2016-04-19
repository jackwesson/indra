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
        if '@' in email:
            u = User.objects.create_user(username=username, email=email, password=password)
            u.save()
            request.session['mid'] = u.id
            return HttpResponseRedirect ('/profilepage/')
        else:
            return render(request, 'index.html', {'errors': 'Enter a valid E-mail Address'})

    
