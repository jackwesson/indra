

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

from .forms import UploadPictureForm, UploadMusicForm, UploadBlurbForm
from .models import Profile, music, description

def index(request, person = ''):
    if person == '':
        user = request.user
        
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        print ('cadlkfjasldfjslkfj;lsakdj')
        print (userobj)
        print ('1')
       
        # username = None
        # if request.user.is_authenticated():
        #     username = request.user.username
        
        # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
        # form1 = UploadPictureForm()
        # form2 = UploadMusicForm()
        # form3 = UploadBlurbForm()
      
        
        # passing = {'form1': form1, 'form2': form2, 'form3': form3}
        passing = {'yes'
        
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
    
    else:
        
        user = person
        
        userobj = User.objects.get(username=user)
        print (userobj)
        
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
        return redirect('/profilepage')
    


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
            
    
    
    
    return redirect('/profilepage')
    

def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')
    
    

