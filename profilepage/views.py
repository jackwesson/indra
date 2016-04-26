

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
from .models import Profile, music, description, artistevents
from displaypage.models import connection

from django.core.mail import send_mail

# def index(request, person = ''):
def index(request):
    try:
        if request.session['somethingdone'] == "yes":
            request.session['somethingdone'] = ''
            return redirect('/profilepage/')
    except:
        pass
    
    if request.session['loading'] == '':
    # if person == '':
        user = request.user

        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
       
        passing = {'yes': True} 
        
        passing['user'] = userobj
        
        blurb = False
        pic = False 
        foryou = False
        youon = False
        event = False
        
        # get any descriptions
        try: 
            you = description.objects.get(owner=userobj)
            yourblurb = you.blurb
            blurb = True
            
        except:
            pass
        
        # try:
        try: 
            you2 = Profile.objects.get(owner=userobj)
            pic = True
        except:
            pass
        
            
        # except Profile.DoesNotExist:
        #     pass
        
        if blurb == True:
            passing['blurb'] =  yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        
       
        
        passing['venue'] = False
        if userobj.first_name == 'venue':
            passing['venue'] = True
            yesevents = False
            # try: 
            # x = event.objects.filter(owner=userobj)
            
            try: 
                x = artistevents.objects.all().filter(owner=userobj)
                # print(x)
                allevents = list(x)
                yesevents = True
                
            except:
                pass
            
            if yesevents == True:
                passing['events'] = x
        else:
            requested = False
            booked = False
            try:
                x = artistevents.objects.all().filter(interested=userobj)
                requested = True
            except:
                pass
            try:
                y = artistevents.objects.all().filter(chosen=userobj)
                booked = True
            except:
                pass
            if requested == True:
                passing['requested'] = x
            if booked == True:
                passing['booked'] = y
                
        
        print (passing)
        return render(request, 'profile.html', passing)
    
    else:
        
        # user = person
        # print ('this is the user')
        # print (user)
        
        # userobj = User.objects.get(username=user)
        userobj = User.objects.get(id=request.session['loading'])
        
        request.session['id2'] = userobj.id
        
        passing = {'yes': False} 
        passing['user'] = userobj
        
        blurb = False
        pic = False 
        try: 
            
            x = artistevents.objects.all().filter(owner=userobj)
            # print(x)
            allevents = list(x)
            yesevents = True
            
            
            
            # except:
            #     pass
            # print(x.event_description)
        except:
            pass
        if yesevents == True:
                passing['events'] = x
        
        
        try: 
            
            you = description.objects.get(owner=userobj)
            
            yourblurb = you.blurb
            blurb = True
            
        except description.DoesNotExist: 
            pass
        
        try:
            
            you2 = Profile.objects.get(owner=userobj)
            
            pic = True
            you2 = Profile.objects.get(owner=userobj)
            pic = True
        except Profile.DoesNotExist:
            pass
        
        if blurb == True:
        
            passing['blurb'] =  yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        
        
        return render(request, 'profile.html', passing)
    


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.FileField
# https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/
# http://stackoverflow.com/questions/4271686/object-has-no-attribute-save-django

# https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/ this links helps with uploading files from forms 

# http://masteringdjango.com/user-authentication-in-django/ more user authentication tools 

# http://stackoverflow.com/questions/7428245/model-form-save-get-the-saved-object this shows how to get your object from the saved form 

def addpic(request):
    if request.method == 'POST':
        
        pic = request.FILES['pic']
        
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        
        
        try:
            obj = Profile.objects.get(owner = userobj)
            
            obj.profilepicture = pic
            obj.save()
            
        except:
            
            obj = Profile(owner=userobj, profilepicture = pic)
            obj.save()
            
        # obj, created = Profile.objects.update_or_create(owner=current_user,
        #                                                 defaults = {"profilepicture" : pic})
        # obj.save()
        
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
        
        price = request.POST.get('price')
        
        event_desc = request.POST.get('eventdesc')
        
        uid = request.session['mid']
        userobj = User.objects.get(id = uid)
        
        new_event = artistevents(owner = userobj, event_name = eventname, date = date, price = price, event_description = event_desc)
        new_event.save()
        request.session['somethingdone'] = 'yes'
        
        return index(request)
        

def deleteconnection(request):
    connect = request.POST['connect_id']
    connectide = connection.objects.get(id = connect)
    connectide.delete()
    request.session['somethingdone'] = 'yes'
    return index(request)
    

def deleteevent(request):
    event = request.POST['event_id']
    eventide = artistevents.objects.get(id = event)
    eventide.delete()
    request.session['somethingdone'] = 'yes'
    return index(request)
    
def selectapplicant(request):
    applicantid = request.POST['app_id']
    eventid = request.POST['event_id']
    applicant = User.objects.get(id = applicantid)
    
    event = artistevents.objects.get(id=eventid)
    event.chosen = applicant
    to_email = ['warren.buhler@yale.edu']
    from_email = 'yaleindramusicteam@gmail.com'
    
    # send_mail('Someone just booked an event', 'yaha', 'yaleindramusicteam@gmail.com', to_email, fail_silently= False)
    
    for x in event.interested.all():
        event.interested.remove(x)
    
    
    event.save()
    
    
    request.session['somethingdone'] = 'yes'
    return index(request)
    
    # the rest of this has yet to be implemented
def loadartist(request):
    applicantid = request.Post['app_id']
    usera = User.objects.get(id = applicantid)
    return index(request, usera)
    
# this is some idea code for soundcloud links

def soundcloudupload(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        
        try:
            linkobj = Links.objects.get(owner=userobj)
            linkobj.link = link
            linkobj.save() 
           
        except:
            new_link = description(owner = userobj, link = link)
            new_link.save() 
            
    request.session['somethingdone'] = 'yes'
        
    return index(request)
    


    
 # sourcelist = []
        # if foryou == True:
        #     sourcelist = sourcelist + list(toyou)
    
        # if youon == True:
            
        #     sourcelist = sourcelist + list(fromyou)
        # if len(sourcelist) > 0:
        #     print('3')
        #     passing['connects'] = sourcelist
        

# if request.method == 'POST':
        
#         pic = request.FILES['pic']
        
#         current_user = request.user
#         obj, created = Profile.objects.update_or_create(owner=current_user,
#                                                         defaults = {"profilepicture" : pic})
       
               
#         form = UploadPictureForm()
#     # return HttpResponse('stuff happened')
#         request.session['somethingdone'] = 'yes'
#         return index(request)