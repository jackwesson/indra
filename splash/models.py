from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django import forms

# Create your models here.

class Splash(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=500)

# class FullUser(AbstractBaseUser):
#     email = models.EmailField('email address', unique=True, db_index=True)
#     joined = models.DateTimeField(auto_now_add=True)
#     usertype = (
#         ('entertainer', "Entertainer"),
#         ('venue', "Venue")
#         )
#     USERNAME_FIELD = 'email'


# http://stackoverflow.com/questions/6963252/onetoone-relation-with-the-user-model-django-contrib-auth-without-cascading-de

# https://www.turnkeylinux.org/blog/django-profile

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="User", null=True, blank=True)
    usertype = (
        ('entertainer', "Entertainer"),
        ('venue', "Venue"),
        )
    profilepicture = forms.FileField()
    themesong = forms.FileField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    