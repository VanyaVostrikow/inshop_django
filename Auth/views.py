from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib import sessions
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest
from .forms import UserLoginForm
from .forms import UserRegistrForm
from django.http import JsonResponse


# Create your views here.

class MainView(TemplateView):
    template_name  = 'Auth/MainAuth.html'
    
def get(self, request: HttpRequest):
        print(request.user)
        if request.user.is_authenticated:
            user = request.user
            humans = User.objects.all()
            ctx = {}
            ctx['humans'] = humans
            ctx['user'] = user
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})
            

class RegisterFormView(FormView):
    
    form_class = UserRegistrForm
    success_url = "/userauth/login/"
    template_name = "Auth/register.html"
    def validate_username(request):
    #"""Проверка доступности логина"""
        username = request.GET.get('username', None)
        response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
        }
        return JsonResponse(response)
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
    

def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'Auth/login.html', {'form': form})
    if request.method == 'POST':
     
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/main/product')
            else:
                print('User not found')
        else:
            print('incorrectdata')
            return render(request, 'Auth/login.html', {'form': form})
        

def logoutView(request):
    logout(request)
    return(redirect('/main/'))
