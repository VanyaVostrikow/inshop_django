from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Coupon
from django import forms
from .forms import CouponApplyForm, CouponSearchForm
import json
from telebot import types
from django.views.decorators.csrf import csrf_exempt
from Telegramm.models import TelegrammUser
import requests
from bot.images import images


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except ObjectDoesNotExist:
            error_coupon = "Doesn't EXIST"
            request.session['coupon_id'] = None
    return redirect('Cart:detail')
@require_POST
@csrf_exempt
def coupon_create_game(request):
    s = request.session 
    Ntry = s.get('Ntry')
    Ntry = str(Ntry)
    user = request.user.username
    owner = None
    user = str(user)
    print(Ntry, user)
    now = datetime.now()
    after_day = now + timedelta(days=5)
    try:                                            #Rewrite COUPON
        coupon = Coupon.objects.get(owner=user)
        hash = s.get('_auth_user_hash')[:5]
        ans = s.get('ans')
        ans = ans[0]+ans[1]+ans[2]+ans[3]
        coupon.code = user + Ntry + hash + ans
        coupon.discount = 20
        coupon.valid_from = now
        coupon.valid_to = after_day
        coupon.active = True
        coupon.save()
        return redirect('Cart:detail')
    except:                                             #New COUPON
        coupon = Coupon()
        coupon.owner = user
        hash = s.get('_auth_user_hash')[:5]
        ans = s.get('ans')
        ans = ans[0]+ans[1]+ans[2]+ans[3]
        coupon.code = user + Ntry + hash + ans
        print(coupon.code)
        coupon.discount = 20
        coupon.valid_from = now
        coupon.valid_to = after_day
        coupon.active = True
        coupon.save()
        return redirect('Cart:detail')
            

@require_POST
def SearchCoupon(request):
    code = {}
    form = CouponSearchForm(request.POST)
    if form.is_valid():
        login = form.cleaned_data['login']
        try:
            q1 = Coupon.objects.filter(owner=login)
            q2 = q1.exclude(valid_from = datetime.now())[:1]
            print(q2.get())
        except ObjectDoesNotExist:
            print("X")
            error_coupon = "Doesn't EXIST"
        return redirect('Main:Products')



@csrf_exempt
def SearchCouponBot(request):
    if request.method == "GET": #Проверка работы бота
        data = {
            "asd":123
        }
        resp = json.dumps(data) #ресопнс
        return HttpResponse(resp)
    if request.method == "POST":
        img = images()
        data = json.loads(request.body.decode()) #получаем пост
        chat_id = str(data['owner']['chat_id']) #получаем айди чата для отправки сообщения
        s = request.session
        print(s.items())
        try:                                                                                    #пытаемся найти пользователя в активированых
            Teleuser_id = TelegrammUser.objects.get(chat_id=chat_id)         #вытаскиваем логин на сайте пользователя из базы по чат айди
            name = Teleuser_id.user                                           #получаем логин на сайте
            print(1)
            try:
                coupon = Coupon.objects.get(owner=name).code  
                active = Coupon.objects.get(owner=name).active
                print(2)
            except:
                coupon = None
            if coupon != None:                                                   
                url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Ваш%20купон:%20' + coupon)      
                print(url)
                print(url)
                
                
                resp = requests.get(url)
                uname = json.loads(resp.text)
                
            else: 
                url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=У%20Вас%20нет%20действительных%20купонов!%20')      
                resp = requests.get(url)
                
                
        except:
            url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Ваш%20Аккаунт%20не%20активирован%20!%20')      
            resp = requests.get(url)



            
    return HttpResponse(chat_id)

