
from os import name
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.get_index, name = 'home'),
]