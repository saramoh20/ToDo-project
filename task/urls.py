from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home),
    path('logup', views.logup),
    path('login', views.login),
    path('search', views.search),
    path('taskes', views.taskes),
]
