from django.shortcuts import render

from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout as pooplogout
from django.db.models import Q
from django.shortcuts import render_to_response, redirect

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from models import connection


from django.http import HttpResponse



# Create your views here.
def index(request):
    if request.method == "POST":
        return redirect('/displaypage')
    artists = User.objects.all()
    content = artists
    
    
    
    # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
    context = {'artists': artists}
    return render(request, 'display.html', context)
        
    
        # return render(request, 'tasks.html', {'query_results': yourtasks}, {'form': form})
        
def loadprofile(request):
    from profilepage.views import index as index2
    if request.method == "POST":
        usera = request.POST.get('artistprofile')
        
        usera = User.objects.get(id = usera)
        return index2(request, usera)
        
        # django templates bulletins url
def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')

def search(request):
    if request.method == 'POST':
        if request.POST['usertype'] == 'venue':
            artists = User.objects.filter(first_name = "venue")
            context = {'artists': artists}
            return render(request, 'display.html', context)
        elif request.POST['usertype'] == 'entertainer':
            artists = User.objects.filter(first_name = "entertainer")
            context = {'artists': artists}
            return render(request, 'display.html', context)
        else:    
            artists = User.objects.all()
            context = {'artists': artists}
            return render(request, 'display.html', context)

def connect(request):
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    
    uid2 = request.session['id2']
    userobj2 = User.objects.get(id=uid2)
    
    new_connection = connection(target = userobj2, originator = userobj)
    new_connection.save()
    print ('it made it !!!!')
    return redirect('/displaypage/loaddisplay')
    