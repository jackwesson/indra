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





def landing(request):
    
    return render(request, 'index.html')
    
    
def thanks(request):
    email = request.POST['email']
    if email != "":
        u = User.objects.create_user(username=email, email=email)
        u.save()
        return render(request, 'thanks.html')
    else:
        
        return render(request, 'index.html')
# def login(request):
# # This function allows the user to login
#     user = request.POST.get('email', '')
#     password = request.POST.get('password', '')
#     # authenticate is a django preset function
#     user = authenticate(username=user, password=password)
#     if user is not None:
#         if user.is_active:
#             django_login(request, user)
#             request.session['mid'] = user.id
#             # request.session['mid'] can be used to identify the user later
#             return HttpResponseRedirect ('/tasks/')
#     else:
       
#         return HttpResponse("Sorry your login information was wrong")
    

def register(request):
    # if (request.POST.get('password', '') == request.POST.get('password_confirmation', '')):
    email = request.POST.get('email', '')
    name = request.POST.get('name', '')
        # password = request.POST.get('password', '')
        
        
        # The user model is a preset django model
    try:
        user = User.objects.create_user(username=email, email=email, first_name=name)
        user.save()
        
        return HttpResponseRedirect ('/')
        
    except:
        return HttpResponse("Sorry please try again with different inputs")
        
    # else:
    #     # print request.POST.get('password', '')
    #     # print request.POST.get('password_confirmation', '')
    #     return HttpResponse("your password and confirmation did not match")
    
    # return render(request, 'djangosocialtwodo/splash.html')
    # return render_to_response('djangosocialtwodo/splash.html', {}, RequestContext(request))
    #return HttpResponse("Hello, world. You're at the splash index.")
    