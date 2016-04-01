

from django.shortcuts import render

# from video https://www.youtube.com/watch?v=Txxa-NP1gXs&list=PLei96ZX_m9sXxvAlhV6El4HnpaClQOXa9&index=2
from django.shortcuts import render_to_response
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

from .forms import UploadPictureForm, UploadMusicForm
from .models import profile, music

def index(request):
    if request.method == 'POST':
        return HttpResponse('stuff happened')
    else:
        uid = request.session['mid']
        # userobj = User.objects.get(id=uid)
       
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        
        # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
        form1 = UploadPictureForm()
        form2 = UploadMusicForm()
       
        userobj = User.objects.get(id=uid)
        
        
        try:
            
            pic = profile.profilepicture
            profile = yourprofile
            pic = profile.profilepicture
            
            passing = {'form1': form1, 'form2': form2, 'pic': pic}
            e
        except:
            passing = {'form1': form1, 'form2': form2}
       
        
       
        return render(request, 'profile.html', passing)
        # return render(request, 'tasks.html', {'query_results': yourtasks}, {'form': form})


# https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.FileField
# https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/
# http://stackoverflow.com/questions/4271686/object-has-no-attribute-save-django

# https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/ this links helps with uploading files from forms 

# http://masteringdjango.com/user-authentication-in-django/ more user authentication tools 

# http://stackoverflow.com/questions/7428245/model-form-save-get-the-saved-object this shows how to get your object from the saved form 

def addpic(request):
    if request.method == 'POST':
        form =UploadPictureForm(request.POST, request.FILES)
        uid = request.session['mid']
        
        if form.is_valid():
            # file is saved
            m = form.save()
            m.user = User.objects.get(id=uid)
            m.save()
            
    
    form = UploadPictureForm()
    # return HttpResponse('stuff happened')
    return render(request, 'profile.html', {'form': form})
    


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