from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.splash, name='splash'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^register/$', views.register, name = 'register'),
    # url(r'up', views.say_whatsup, name='whatsup'),
]

