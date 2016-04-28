from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^mrw/', views.mrw, name = 'mrw'),
    url(r'^foo/', views.foo, name = 'foo'),


]
