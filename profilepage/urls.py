from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addpic/$', views.addpic, name = 'addpic'),
]