from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^maxlogout/$', views.maxlogout, name='maxlogout'),
    url(r'^addtask/$', views.addtask, name='addtask'),
    url(r'^makecomplete/$', views.makecomplete, name='makecomplete'),
    url(r'^delete/$', views.delete, name='delete'),
    
]

