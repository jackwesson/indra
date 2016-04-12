from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addpic/$', views.addpic, name = 'addpic'),
    url(r'^addmusic/$', views.addmusic, name = 'addmusic'),
    url(r'addblurb/$', views.addblurb, name = 'addblurb'),

]