from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from Coupon.models import Coupon
import json
from telebot import types

import telebot
import traceback
from Telegramm.models import TelegrammUser
from bot.images import images

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            user = request.user.username
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.owner = user
            order.save()
               
                
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            code = cart.coupon
            try:
                coupon = Coupon.objects.get(code=code)
                coupon.active = False
                coupon.save()
            except:
                print('no')
            order_created.delay(order.id)
            return render(request, 'Order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'Order/create.html',
                  {'cart': cart, 'form': form})

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
        
        try:                                                                                    #пытаемся найти пользователя в активированых
            Teleuser_id = TelegrammUser.objects.get(chat_id=chat_id)         #вытаскиваем логин на сайте пользователя из базы по тг-логину
            name = Teleuser_id.user                                           #получаем логин на сайте
            print(name)
            print(chat_id)
            all_orders = Order.objects.filter(owner=name)
            print(len(all_orders))
            all_orders_list = []
            for i in range(len(all_orders)):
                n = all_orders.__dict__['_result_cache']
                all_orders_list.append(n[i])
            
            keyboard = types.InlineKeyboardMarkup()
            for i in range(len(all_orders_list)):
                num = 0
                num = str(all_orders_list[i])
                print(type(num))
                keyboard.add(types.InlineKeyboardButton(text=num, callback_data=num))
            keyboard = keyboard.to_json()
            if len(all_orders_list) != 0:
                                                               
                url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Ваш%20заказ:%20' + "&reply_markup=" + keyboard)
              
                print(url)
                resp = requests.get(url)
                uname = json.loads(resp.text)
               
            else: 
                url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['notknow'] + '&caption=У%20Вас%20нет%20заказов!')      
                resp = requests.get(url)
                uname = json.loads(resp.text)
                
        except Exception as e:
            print(traceback.format_exc())
            url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['hello'] + '&caption=Ваш%20Аккаунт%20не%20активирован%20!%20')      
            resp = requests.get(url)
            uname = json.loads(resp.text)
            tgname = uname.get('result')
    return HttpResponse(chat_id)

@csrf_exempt
def order_detail(request):
    if request.method == 'POST':
        img = images()
        data = json.loads(request.body.decode()) #получаем пост
        order_id = str(data['order_id']) #получаем айди чата для отправки сообщения
        chat_id = str(data['chat_id'])

        order = Order.objects.get(id=order_id)
        print(order, chat_id)
        paid = order.paid
        city = order.city
        first_name = order.first_name
        last_name = order.last_name
        email = order.email
        url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Номер%20заказа:%20' + order_id + '\nИмя%20заказчика:%20' + first_name + '\nФамилия%20Заказчика:%20' + last_name + '\nГород%20Доставки:%20' + city)
        resp = requests.get(url)
    return HttpResponse(order_id)
     