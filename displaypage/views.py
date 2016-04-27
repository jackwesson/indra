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

from profilepage.models import artistevents

from django.http import HttpResponse

# this code runs when displaypage is loaded
def index(request):
    request.session['loading'] = ''
    if request.method == "POST":
        return redirect('/displaypage')
    
    # this code is designed to work with the search function, the search function did not make it into the MVP we posted 
    # try:
    #     if request.session['search'] == 'venue':
    #         artists = User.objects.filter(first_name = "venue")
    #         context = {'artists': artists}
    #         request.session['search'] = ''
    #         return render(request, 'display.html', context)
    #     elif request.session['search'] == 'entertainer':
    #         artists = User.objects.filter(first_name = "entertainer")
    #         context = {'artists': artists}
    #         request.session['search'] = ''
    #         return render(request, 'display.html', context)
       
    # except:
    #     pass
    
    
    # get all the users in the Indra community
    artists = User.objects.all()
    content = artists
    context = {'artists': content}
    
    
    # get all the events
    try: 
        events = artistevents.objects.all()
        hoop = list(events)
        
        context = {'artists': content, 'events': events}
    except:
        pass
    
    return render(request, 'display.html', context)
        
    
        
# this enable the user to load the page of a Indra community member they are interested in  
def loadprofile(request):
    from profilepage.views import index as index2
    if request.method == "POST":
        usera = request.POST.get('artistprofile')
        
        usera = User.objects.get(id = usera)
        
        
        request.session['loading'] = usera.id
        # return index2(request, usera)
        return index2(request)
    if request.method == "GET":
        return index2(request)
        
# logout function
def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')

# from the load profile page, the user can apply to be considered for posted events 
def applyevent(request):
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    
    
    event = request.POST['event_id']
    eventide = artistevents.objects.get(id = event)
    eventide.interested.add(userobj)
    
    eventide.save()
    request.session['loading'] = ''
    return redirect('/profilepage')

# allows the user to load his own profile from the display page
def loadownprofile(request):
    request.session['loading'] = ''
    return redirect('/profilepage')
    
    
# this is old code from before events, we are leaving it as is in case we want to allow users more ability to interact with each other
def connect(request):
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    
    uid2 = request.session['id2']
    userobj2 = User.objects.get(id=uid2)
    
    
    new_connection = connection(target = userobj2, originator = userobj)
    new_connection.save()
    # new_connection.originator.add(userobj) 
    # new_connection.save()

# this allows the user to search for venues or artists, the implementation did not make it into the mvp
def search(request):
    
    request.session['search'] = request.POST['usertype']
    return index(request)
    return redirect('/profilepage')