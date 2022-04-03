from os import name
from django.urls import path
from . import views

app_name = 'aboutus'
urlpatterns = [
    path('', views.get_aboutus, name = 'aboutus'),
]