

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
from .models import Profile, music, description, artistevents, artistlinks
from displaypage.models import connection

from django.core.mail import send_mail

# this is the code that runs when the profile page is loaded
def index(request):
    # this try statement checks to see if something has been changed, if so it redirects the url - this enables me to load the profile page url after calling a function
    try:
        if request.session['somethingdone'] == "yes":
            request.session['somethingdone'] = ''
            return redirect('/profilepage/')
    except:
        pass
    
    # if index is being called through loaddisplay, 'loading' will not be nothing , if it is nothing the user owns the profile page
    
    if request.session['loading'] == '':
    
        user = request.user

        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
       
    #   yes as true tells the html if statements to load the inputs neccesary for the owner to manipulate his profile page
        passing = {'yes': True} 
        
        passing['user'] = userobj
        
        blurb = False
        pic = False 
        foryou = False
        youon = False
        event = False
        linked = False
        
        # get anything associated with the owner of the profile page
        try: 
            you = description.objects.get(owner=userobj)
            yourblurb = you.blurb
            blurb = True
            
        except:
            pass
        
        try: 
            artlink = artistlinks.objects.get(owner=userobj)
            artlink = artlink.link
            linked = True
            
        except:
            pass
        
        
        try: 
            you2 = Profile.objects.get(owner=userobj)
            pic = True
        except:
            pass
        
            
       
        
        if blurb == True:
            passing['blurb'] = yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        if linked == True:
            passing['link'] = artlink
        
       
        # check to see if the user is a venue, if so, load all events he owns and tell the html to load the event input form
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
        # if not a venue, load all the events applied to and selected for 
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
                
        
        
        return render(request, 'profile.html', passing)
    
    # if request.session['loading'] is not empty string, load the profile associated with that id
    else:
       
        userobj = User.objects.get(id=request.session['loading'])
        
        request.session['id2'] = userobj.id
        
        passing = {'yes': False} 
        passing['user'] = userobj
        
        blurb = False
        pic = False 
        
        try: 
            x = artistevents.objects.all().filter(owner=userobj)
            allevents = list(x)
            yesevents = True
            
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
            
        except Profile.DoesNotExist:
            pass
        
        if blurb == True:
            passing['blurb'] =  yourblurb
        
        if pic == True:
            yourpic = you2.profilepicture
            passing['pic'] =  yourpic
        
        
        return render(request, 'profile.html', passing)
    




# this allows you to load a profile picture for your profile page

def addpic(request):
    if request.method == 'POST':
        
        pic = request.FILES['pic']
        
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        
        # alter or create existing 
        try:
            obj = Profile.objects.get(owner = userobj)
            
            obj.profilepicture = pic
            obj.save()
            
        except:
            
            obj = Profile(owner=userobj, profilepicture = pic)
            obj.save()
        
    # set something done to yes in order to tell index to redirect
        request.session['somethingdone'] = 'yes'
        return index(request)
    
    
    # this code enables you to add a blurb to your profile page
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
    
    

# enables log out
def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')
    
# redirects user to the display page with all the events and artists
def loaddisplay(request):
    from displaypage.views import index as index2
    if request.method == "POST":
        return index2(request)

# this allows the user to create events, multiple events can be created for each user
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
        
    
# can be used to delete events 
def deleteevent(request):
    event = request.POST['event_id']
    eventide = artistevents.objects.get(id = event)
    eventide.delete()
    request.session['somethingdone'] = 'yes'
    return index(request)
    
    
#   each applicant to an event will be displayed, this code allows the user to select which artist they want to contract with 
def selectapplicant(request):
    applicantid = request.POST['app_id']
    eventid = request.POST['event_id']
    applicant = User.objects.get(id = applicantid)
    event = artistevents.objects.get(id=eventid)
    event.chosen = applicant
    
    # this code sends our email account a notice with the username and email of the venue and entertainer, we can then facilitate the proccess
    to_email = ['yaleindramusicteam@gmail.com']
    from_email = 'yaleindramusicteam@gmail.com'
    body = ' The venue ' + str(event.owner.username) +  ' ' + str(event.owner.email) + '  just booked and event with' + str(applicant.username) + ' ' + str(applicant.email)
    
    send_mail('Someone just booked an event', body, from_email, to_email, fail_silently= True)
    
    # must remove all interested parties one at a time from the event 
    for x in event.interested.all():
        event.interested.remove(x)
    
    # save the event in its new state
    event.save()

    request.session['somethingdone'] = 'yes'
    return index(request)
    

# this allows artsit to submit links to their soundcloud page
def soundcloudupload(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        
        try:
            linkobj = artistlinks.objects.get(owner=userobj)
            linkobj.link = link
            linkobj.save() 
           
        except:
            new_link = artistlinks(owner = userobj, link = link)
            new_link.save() 
            
    request.session['somethingdone'] = 'yes'
        
    return index(request)
    
    
   # this is the beginning of code that would allow a venue to click and look at the artist who applied or their event
def loadartist(request):
    applicantid = request.Post['app_id']
    usera = User.objects.get(id = applicantid)
    return index(request, usera)

 # this is starter code that is unimplemented for saving music directly
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

#  connections is old code that predates our decision to use events, I am leaving it in case we decide we want more user interaction on the site
def deleteconnection(request):
    connect = request.POST['connect_id']
    connectide = connection.objects.get(id = connect)
    connectide.delete()
    request.session['somethingdone'] = 'yes'
    return index(request)