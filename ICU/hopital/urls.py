
from os import name
from django.urls import path
from . import views

app_name = 'hopital'
urlpatterns = [
    path('', views.get_profile, name = 'profile'),
]