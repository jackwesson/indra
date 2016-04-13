from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login, name = 'login'),

    # url(r'^login/$', views.login, name = 'login'),
    # url(r'up', views.say_whatsup, name='whatsup'),
]

