from django.shortcuts import render, HttpResponse
from django.shortcuts import render
import json
from Telegramm.models import TelegrammUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Order.models import Order, OrderItem
from Coupon.models import Coupon
from django.contrib.auth.models import User


def api_coupon(request):
    body = request
    chat_id = body.GET.get('chat_id')
    Teleuser_id = TelegrammUser.objects.get(chat_id=chat_id)         #вытаскиваем логин на сайте пользователя из базы по чат айди
    name = Teleuser_id.user
    model = Coupon.objects.filter(owner=name)
    coupon = model.get.all()
    print(coupon)
    return HttpResponse()

def api_view_coupon():

    return Response({})

def api_create_coupon():

    return Response({})

def api_delete_coupon():

    return Response({})

def api_change_coupon():

    return Response({})


def api_view_order():

    return Response({})

def api_create_order():

    return Response({})

def api_delete_order():

    return Response({})

def api_change_order():

    return Response({})



def api_view_user():

    return Response({})

def api_create_user():

    return Response({})

def api_delete_user():

    return Response({})

def api_change_user():

    return Response({})

# Create your views here.
