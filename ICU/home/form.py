import email
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms 

text = {}

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20, widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control'}))

class loginForm(forms.Form):
    username = forms.CharField(max_length = 20, widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs={'class':'form-control'}))