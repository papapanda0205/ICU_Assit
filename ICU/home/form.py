from django import forms 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

text = {}

class registerForm(UserCreationForm):
    username = forms.CharField(max_length = 20, widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class loginForm(forms.Form):
    username = forms.CharField(max_length = 20, widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control'}))

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length = 20, widget= forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))

    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length = 20, widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length = 100, widget= forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'first_name', 'password')