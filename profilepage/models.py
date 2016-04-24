from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.conf import settings



# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, related_name="profile_picture")
    profilepicture = models.ImageField(upload_to="propics")
    
class music(models.Model):
    owner = models.ForeignKey(User, related_name="example_music")
    examplemusic = models.FileField(upload_to='uploads/')
    
class description(models.Model):
    owner = models.ForeignKey(User, related_name="band_name", primary_key = True)
    blurb = models.CharField(max_length=100)


class venueevents(models.Model):
    owner = models.ForeignKey(User, related_name="venue_name", unique = False)
    event_name = models.CharField(max_length = 100)
    event_description = models.CharField(max_length = 200)
    date = models.DateField()
    price = models.CharField(max_length = 20)
    applicants = models.ManyToManyField(User, related_name="applicants")
    chosen = models.ForeignKey(User, related_name="chosen", unique = False, null = True)