from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *


class LoginForm(forms.Form):
    username=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

# class RegistrationForm(forms.ModelForm):
#     first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter Your first name'}),required=True)

#     last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter Your Last name'}),required=True)

#     email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg-abc@gmail.com'}),required=True)

#     username=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter Your username'}),required=True)

#     gender=forms.ChoiceField(choices=Profile.Gen_Choice,widget=forms.Select(attrs={'placeholder':'Enter Your Gender'}),required=True)

#     password=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'placeholder':"enter your password"}))

#     confirm_password=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'placeholder':"confirm password"}))

#     class Meta:
#         model=User
#         fields=['first_name','last_name','email','username']

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
    
class ProfileRegistrationForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Profile.Gen_Choice,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model=Profile
        fields=['gender']

class UserUpdateForm(forms.Form):
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'name':'first_name','class':'form-control'}))        
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'name':'last_name','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'name' :'email','class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'name':'username','class':'form-control'}))
    gender=forms.ChoiceField(choices=Profile.Gen_Choice,widget=forms.Select(attrs={'name':'gender','class':'form-control'}))
    class Meta:
        fields=['first_name','last_name','email','username','gender']
