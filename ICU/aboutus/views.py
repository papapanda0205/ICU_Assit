from cgitb import html
import imp
from django.shortcuts import render
from django.http import HttpResponse

def get_aboutus(request):
    return render (request, 'aboutus/member.html')
