from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import sessions
from django.contrib.auth import login, logout, authenticate
from Order.models import OrderItem
# Create your views here.




def ProfileView(request):
    error = ''
    
    if request.user.is_authenticated:
        user_id = request.user.id
        print(user_id)
        user = request.user.username
        mail = request.user.email
        context = {'user':user, 'mail':mail}
    else:     
        user = request.user.username
        error = "ONLY FOR LOGGIN USER! WANNA LOGIN?"
        context = {'error':error}
    return render(request, 'profile_view.html', context)
    