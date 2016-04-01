from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login as django_login, logout as pooplogout
from django.db.models import Q


from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


from django.http import HttpResponse



# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse('stuff happened')
    else:
        artists = User.objects.all()
        content = artists
        
        
        
        # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
        context = {'artists': artists}
        return render(request, 'display.html', context)
        
    
        # return render(request, 'tasks.html', {'query_results': yourtasks}, {'form': form})