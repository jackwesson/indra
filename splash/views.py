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
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST or None)
    #     form2 = RegisterForm(request.POST or None)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         new_splash, created = User.objects.get_or_create(username = email, email=email, password=password)
    #         print new_splash, created
    #         return HttpResponse('done!')

    # if a GET (or any other method) we'll create a blank form
    # else:
    form = NameForm()
    form2 = RegisterForm()

    return render(request, 'name.html', {'form': form, 'form2': form2})
    
def login(request):

    user = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = authenticate(username=user, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            request.session['mid'] = user.id
            # return HttpResponse("You are now logged in")
            return HttpResponseRedirect ('/tasks/')
    else:
        # return render(request, "name.html", {'errors': "Your login was wrong"})
        return HttpResponse("Sorry your login was wrong")
    
    # template = get_template('djangosocialtwodo/splash.html')
    # return HttpResponse(render(template, request))

def register(request):
    if (request.POST.get('password', '') == request.POST.get('password_confirmation', '')):
        email = request.POST.get('email', '')
        fname = request.POST.get('first', '')
        lname = request.POST.get('last', '')
        password = request.POST.get('password', '')
        
        # if User.objects.filter(email).exists():
        #     return HttpResponse("you are already in the system")
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
            return HttpResponse("It didn't work")
        
    else:
        # print request.POST.get('password', '')
        # print request.POST.get('password_confirmation', '')
        return HttpResponse("your password and confirmation did not match")
    
    # return render(request, 'djangosocialtwodo/splash.html')
    # return render_to_response('djangosocialtwodo/splash.html', {}, RequestContext(request))
    #return HttpResponse("Hello, world. You're at the splash index.")
    