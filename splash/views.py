#original 
from django.shortcuts import render

# from video https://www.youtube.com/watch?v=Txxa-NP1gXs&list=PLei96ZX_m9sXxvAlhV6El4HnpaClQOXa9&index=2
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout

# working with forms
from .forms import NameForm
from .forms import RegisterForm

#original
from django.http import HttpResponse

# Create your views here.


#  https://www.youtube.com/watch?v=VtNHVuJq93U
# potentially useful video series


def splash(request):
    # This displays the template of register and login
    form = NameForm()
    form2 = RegisterForm()

    return render(request, 'name.html', {'form': form, 'form2': form2})
    
def login(request):
# This function allows the user to login
    user = request.POST.get('email', '')
    password = request.POST.get('password', '')
    # authenticate is a django preset function
    user = authenticate(username=user, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            request.session['mid'] = user.id
            # request.session['mid'] can be used to identify the user later
            return HttpResponseRedirect ('/tasks/')
    else:
       
        return HttpResponse("Sorry your login information was wrong")
    

def register(request):
    if (request.POST.get('password', '') == request.POST.get('password_confirmation', '')):
        email = request.POST.get('email', '')
        fname = request.POST.get('first', '')
        lname = request.POST.get('last', '')
        password = request.POST.get('password', '')
        
        
        # The user model is a preset django model
        try:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    # return HttpResponse("You are now logged in")
                    request.session['mid'] = user.id
                    return HttpResponseRedirect ('/tasks/')
            
        except:
            return HttpResponse("Sorry please try again with different inputs")
        
    else:
        # print request.POST.get('password', '')
        # print request.POST.get('password_confirmation', '')
        return HttpResponse("your password and confirmation did not match")
    
    # return render(request, 'djangosocialtwodo/splash.html')
    # return render_to_response('djangosocialtwodo/splash.html', {}, RequestContext(request))
    #return HttpResponse("Hello, world. You're at the splash index.")
    