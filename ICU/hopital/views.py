from cgitb import html
import imp
from django.shortcuts import render
from django.http import HttpResponse

def get_profile(request):
    return render (request, 'hopital/profile.html')
