from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    tasks = None
    return render(request, 'index.html', {'tasks': tasks})

def foo(request):
#logs in users/ directed here from register
    if request.method == 'GET':
            return HttpResponse("The brute lute, Toot, who wears a suit, likes to loot the cute boot, Woot")

def mrw(request):

    return HttpResponseRedirect('https://i.imgur.com/pXjrQ.gif')

def logout_form(request):
    logout(request)
    #django logout
    return HttpResponseRedirect('/')
