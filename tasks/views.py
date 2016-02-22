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
    if request.method == 'POST':
        return HttpResponse('stuff happened')
    else:
        form = TaskForm()
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)
        yourtasks = Task.objects.filter(Q(owner = userobj) | Q(collaborators = userobj))
        content = yourtasks
        
        # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
        
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

    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    # because collaborators is a multi entry field, you have to add collaborators after creating the new task
    # I'm not sure why save goes above adding collaborators, but the code broke when the save was not above
    new_Task = Task(owner=userobj, title=title, description=description)
    new_Task.save()
    if collaborator1 != '':
        
        collaboratored = User.objects.filter(email = collaborator1)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
        
    if collaborator2 != '':
        
        collaboratored = User.objects.filter(email = collaborator2)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
        
    if collaborator3 != '':
        
        collaboratored = User.objects.filter(email = collaborator3)
        coll = collaboratored[0]
        new_Task.collaborators.add(coll)
    # new_Task.save()
    return HttpResponseRedirect ('/tasks/')
   
        
def makecomplete(request):
    task = request.POST["taskID"]
    # check the task id, if complete toggle false, if not complete toggle true
    taskide = Task.objects.get(id = task)
    if taskide.complete == False:
        taskide.complete = True
    else:
        taskide.complete = False
    taskide.save()
    return HttpResponseRedirect ('/tasks/')

def delete(request):
    # delete button would only have displayed if the current user is the owner, so no need to check here
    task = request.POST["taskID"]
    taskide = Task.objects.get(id = task)
    taskide.delete()
    return HttpResponseRedirect ('/tasks/')
    
    
def maxlogout(request):
    pooplogout(request)
    return HttpResponseRedirect ('/')
