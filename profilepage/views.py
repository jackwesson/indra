

from django.shortcuts import render
# from video https://www.youtube.com/watch?v=Txxa-NP1gXs&list=PLei96ZX_m9sXxvAlhV6El4HnpaClQOXa9&index=2
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout as pooplogout
from django.db.models import Q

from django.contrib.sessions.models import Session

from django.http import HttpResponse

from .forms import UploadPictureForm, UploadMusicForm, UploadBlurbForm, UploadEventForm
from .models import Profile, music, description, venueevents
from displaypage.models import connection


def index(request, person = ''):
    try:
        if request.session['somethingdone'] == "yes":
            request.session['somethingdone'] = ''
            return redirect('/profilepage/')
    except:
        pass
    
    if person == '':
        user = request.user
        
        
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
       
        passing = {'yes': True} 
        
        blurb = False
        pic = False 
        foryou = False
        youon = False
        event = False
        
        try: 
            you = description.objects.get(target=userobj)
            yourblurb = you.blurb
            blurb = True
            
        except:
            pass
        try: 
            from displaypage.models import connection
            x = description.objects.filter(Q(originator=userobj))
            fromyou = x 
            print ('should be this')
            print (fromyou)
            youon = True
            
        except: 
            pass
        
        try: 
            from displaypage.models import connection
            y = connection.objects.filter(Q(target=userobj))
            toyou = y
            
            foryou = True
        except description.DoesNotExist: 
            pass
        try:
            you2 = Profile.objects.get(owner=userobj)
            pic = True
        except Profile.DoesNotExist:
            pass
        # try:
        #     allevents = events.objects.filter(owner=userobj)
        #     event = True
        # except 
        #     pass
        # if event == True:
        #     passing['events'] = allevents
        
        
        if blurb == True:
            passing['blurb'] =  yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        sourcelist = []
        if foryou == True:
            sourcelist = sourcelist + list(toyou)
    
        if youon == True:
            
            sourcelist = sourcelist + list(fromyou)
        if len(sourcelist) > 0:
            print('3')
            passing['connects'] = sourcelist
        
        print(userobj.first_name)
        
        if userobj.first_name == 'venue':
            passing['eventform'] = UploadEventForm()
            yesevents = False
            # try: 
            print ('should definitely get here')
            # x = event.objects.filter(owner=userobj)
            
            x = venueevents.objects.all().filter(owner=userobj)
            # print(x)
            allevents = list(x)
            yesevents = True
            print ('definitely to here as well')
            
            # except:
            #     pass
            # print(x.event_description)
            if yesevents == True:
                passing['events'] = x
                
        
        print (passing)
        return render(request, 'profile.html', passing)
    
    else:
        
        user = person
        
        userobj = User.objects.get(username=user)
        request.session['id2'] = userobj.id
        
        passing = {'yes': False} 
        
        blurb = False
        pic = False 
        
        try: 
            
            you = description.objects.get(owner=userobj)
            
            yourblurb = you.blurb
            blurb = True
            
        except description.DoesNotExist: 
            pass
        
        try:
            you2 = Profile.objects.get(owner=userobj)
            
            pic = True
        except Profile.DoesNotExist:
            pass
        
        if blurb == True:
        
            passing['blurb'] =  yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        
        print (passing)
        return render(request, 'profile.html', passing)
    


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.FileField
# https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/
# http://stackoverflow.com/questions/4271686/object-has-no-attribute-save-django

# https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/ this links helps with uploading files from forms 

# http://masteringdjango.com/user-authentication-in-django/ more user authentication tools 

# http://stackoverflow.com/questions/7428245/model-form-save-get-the-saved-object this shows how to get your object from the saved form 

def addpic(request):
    if request.method == 'POST':
        
        # form = UploadPictureForm(request.POST, request.FILES)
        pic = request.FILES['pic']
        
        current_user = request.user
        obj, created = Profile.objects.update_or_create(owner=current_user,
                                                        defaults = {"profilepicture" : pic})
       
        form = UploadPictureForm()
    # return HttpResponse('stuff happened')
        request.session['somethingdone'] = 'yes'
        return index(request)
    


def addmusic(request):
    if request.method == 'POST':
        form =UploadMusicForm(request.POST, request.FILES)
        uid = request.session['mid']
        if form.is_valid():
            # file is saved
            m = form.save()
            m.user = User.objects.get(id=uid)
            m.save()
    
    form = UploadMusicForm()
    # return HttpResponse('stuff happened')
    return render(request, 'profile.html', {'form': form})
    
    
def addblurb(request):
    if request.method == 'POST':
        
        blurb = request.POST.get('blurb')
        uid = request.session['mid']
        
        userobj = User.objects.get(id=uid)
        
        try:
           
            desc = description.objects.get(owner=userobj)
            desc.blurb = blurb
            desc.save() 
            
        except:
            
            new_desc = description(owner = userobj, blurb = blurb)
            new_desc.save() 
            
    request.session['somethingdone'] = 'yes'
        
    return index(request)
    
# def connect(request):
#     uid = request.session['mid']
#     userobj = User.objects.get(id=uid)
    
#     uid2 = request.session['id2']
#     userobj2 = User.objects.get(id=uid2)
    
#     new_connection = connection(target = userobj2, originator = userobj)
#     new_connection.save()
#     print ('it made it !!!!')
#     return redirect('/displaypage/loaddisplay')
    


def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')
    

def loaddisplay(request):
    from displaypage.views import index as index2
    if request.method == "POST":
        return index2(request)

def addevent(request):
    if request.method == "POST":
        eventname = request.POST.get('eventname')
        date = request.POST.get('eventdate')
        print (date)
        price = request.POST.get('price')
        print ('this should be price')
        print (price)
        event_desc = request.POST.get('eventdesc')
        print(event_desc)
        uid = request.session['mid']
        userobj = User.objects.get(id = uid)
        
        new_event = venueevents(owner = userobj, event_name = eventname, date = date, price = price, event_description = event_desc)
        new_event.save()
        request.session['somethingdone'] = 'yes'
        
        return index(request)
        

def deleteconnection(request):
    connect = request.POST['connect_id']
    connectide = connection.objects.get(id = connect)
    connectide.delete()
    return index(request)
    