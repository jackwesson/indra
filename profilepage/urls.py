from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addpic/$', views.addpic, name = 'addpic'),
    url(r'^addmusic/$', views.addmusic, name = 'addmusic'),
    url(r'addblurb/$', views.addblurb, name = 'addblurb'),
    url(r'maxlogout/$', views.maxlogout, name = 'maxlogout'),
    url(r'^loaddisplay/$', views.loaddisplay, name = 'loaddisplay'),
    url(r'^addevent?$', views.addevent, name = 'addevent')
    # url(r'displaypage/loadprofile/connect', views.connect, name = 'connect'),
]