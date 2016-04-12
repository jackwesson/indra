from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^thanks/$', views.thanks, name = 'thanks'),
    url(r'^login/$', views.login, name = 'login'),

    # url(r'^login/$', views.login, name = 'login'),
    # url(r'up', views.say_whatsup, name='whatsup'),
]

