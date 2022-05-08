from re import template
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .form import registerForm, loginForm, PasswordChangingForm, EditProfileForm
from django.views import View
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home:home')

class registerUser(generic.CreateView):
    form_class = registerForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home:loginUser')


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


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'home/edit_profile.html'
    success_url = reverse_lazy('home:profile')

    def get_object(self):
        return self.request.user

