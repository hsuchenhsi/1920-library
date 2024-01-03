from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['booking']




class CustomRegistrationForm(UserCreationForm):

    pass