from .models import Comment, Product
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import login, logout, authenticate

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'PrProd', 'PrUser']
        

        widgets = {
            
            "title": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Put ur Comm',
            })
         
        }

