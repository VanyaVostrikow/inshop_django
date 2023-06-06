from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'text-field__input',
                'placeholder': 'USERNAME', 
                'id': 'inputLogin'
                }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'text-field__input',
            'placeholder': 'PASSWORD',
            'id': 'inputPassword',
        }
    ))
class UserRegistrForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'text-field__input',
                'placeholder': 'USERNAME', 
                'id': 'id_username'
                }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'text-field__input',
            'placeholder': 'PASSWORD',
            'id': 'id_password1',
        }
    ))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'text-field__input',
            'placeholder': 'PASSWORD',
            'id': 'id_password2',
        }
    ))

