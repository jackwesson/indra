from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loadprofile/$', views.loadprofile, name = 'loadprofile'),
    url(r'maxlogout/$', views.maxlogout, name = 'maxlogout'),
]