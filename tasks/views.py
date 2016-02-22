#original 
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

# Create your views here.

from models import Task
from .forms import TaskForm

def index(request):
    # user = request.user.get_username()
    # relevant = Task.objects.filter(Q(owner = user) | Q(collaborators = user))
    # holder = relevant.objects.order_by('title')
    # holder = Task.objects.all()
    # output = ', '.join([p for p in holder])
    # return HttpResponse(output)
    if request.method == 'POST':
        return HttpResponse('stuff happened')
    else:
        form = TaskForm()
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        yourtasks = Task.objects.filter(Q(owner = userobj) | Q(collaborators = userobj))
        content = yourtasks
        
    #     context = {
    #     'latest_question_list': latest_question_list,
    # }
        
        context = {'yourtasks': yourtasks, 'form': form, 'id': userobj}
        return render(request, 'tasks.html', context)
        # return render(request, 'tasks.html', {'query_results': yourtasks}, {'form': form})

def addtask(request):
    # email = request.POST.get('owner', '')
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    collaborator1 = request.POST.get('collaborator1', '')
    collaborator2 = request.POST.get('collaborator2', '')
    collaborator3 = request.POST.get('collaborator3', '')
    # print 'did this work' + collaborator1
    # Test code for getting logged in user
    # http://stackoverflow.com/questions/19805129/get-user-object-using-userid-in-django
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    
    # Moved save to bottom
    new_Task = Task(owner=userobj, title=title, description=description)
    new_Task.save()
    if collaborator1 != '':
        # print collaborator1
        collaboratored = User.objects.filter(email = collaborator1)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
        
    if collaborator2 != '':
        # print collaborator1
        collaboratored = User.objects.filter(email = collaborator2)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
        
    if collaborator3 != '':
        # print collaborator1
        collaboratored = User.objects.filter(email = collaborator3)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
    # new_Task.save()
    return HttpResponseRedirect ('/tasks/')
        
def makecomplete(request):
    task = request.POST["taskID"]
    taskide = Task.objects.get(id = task)
    if taskide.complete == False:
        taskide.complete = True
    else:
        taskide.complete = False
    taskide.save()
    return HttpResponseRedirect ('/tasks/')

def delete(request):
    task = request.POST["taskID"]
    taskide = Task.objects.get(id = task)
    taskide.delete()
    return HttpResponseRedirect ('/tasks/')
    
    
def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')
