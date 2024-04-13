from django import forms
from . models import *


class PostRegistrationForm(forms.ModelForm):
    title=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter your title','class':"form-control"}))
    title_tag=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Enter your title tag','class':"form-control"}))
    body=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your body','class':"form-control"}))
    class Meta:
        model=Post
        fields=['title','title_tag','body']

 
