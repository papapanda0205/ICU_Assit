from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, redirect

from .form import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages


class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'home/register.html', {'rF' : rF})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse ('Register success')

class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render (request, 'home/login.html', {'lF' : lF})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home/view_profile.html')
        else:
            return redirect('home:loginUser')

def logoutUser(request):
    logout(request)
    return redirect('home:loginUser')

@login_required(login_url='/login/')
def get_index(request):
    return render (request, 'home/index.html')

@login_required(login_url='/login/')
def view_profile(request):
    return render (request, 'home/view_profile.html')

def profile(request):
    args = {'user' : request.user}
    return render (request, 'home/view_profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        uf = UserChangeForm(request.POST, instance = request.user)

    if uf.is_valid():
        uf.save()   
        return redirect('home:view_profile')
    else:
        uf = UserChangeForm (instance = request.user)
        args = {'uf' : uf}
        return render(request, 'home/edit_profile.html', args)