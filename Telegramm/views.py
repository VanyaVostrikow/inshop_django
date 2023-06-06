from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from Game.Game import answer
from django.views.decorators.csrf import csrf_exempt
from Telegramm.forms import TeleCodeForm, TeleidForm
from .models import TelegrammUser
import json
from telebot import types
from Order.models import Order
from Coupon.models import Coupon
import traceback
import requests
from bot.images import images
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def activate(request):
    if request.method == 'POST':
        user = request.user
        check = None
        try:
            check = TelegrammUser.objects.get(user=user)
            print("<<<ERROR! USER FOUNDED", check, " >>>")
            
        except:
        
            teleid = request.POST.get('teleid')
            data = {
                    'teleid' : teleid
            }
            code_list = answer()
            code1 = code_list[0] + code_list[1] + code_list[2] + code_list[3]
            request.session['code1'] = code1
            form = TeleidForm(data)
            chat_id = data.get('teleid')
            request.session['chat_id'] = chat_id
            try:
                check = TelegrammUser.objects.get(chat_id=chat_id)
                print("<<<ERROR! CHAT_ID FOUNDED:", check, " >>>")
                check = None
                if user.is_authenticated == False:
                    print('sosiska')
                    teleid = request.POST.get('teleid')
                    data = {
                        'teleid' : teleid
                    }
                    code_list = answer()
                    code1 = code_list[0] + code_list[1] + code_list[2] + code_list[3]
                    request.session['code1'] = code1
                    chat_id = data.get('teleid')
                    url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendMessage?chat_id=' + chat_id + '&text=Ваш%20код%20активации:%20' + code1)   
                    #print(url)
                    resp = requests.get(url)
                    uname = json.loads(resp.text)
                    print('sosiska')
                    return redirect('logintele/')
                else:
                    print("None")
            except:
                request.session['chat_id'] = chat_id
                if form.is_valid():
                    url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendMessage?chat_id=' + chat_id + '&text=Ваш%20код%20активации:%20' + code1)   
                    #print(url)
                    resp = requests.get(url)
                    uname = json.loads(resp.text)
                    tgname = uname.get('result')
                    if tgname:
                        tgname = uname['result']['chat']['username']
                        request.session['tgname']=tgname
                        return redirect('code/')
                    else:
                        context = {
                        'form':form
                        }
                        return render(request, 'activatetg.html', context)
                
    form = TeleidForm
    context = {
        'form':form
    }
    return render(request, 'activatetg.html', context)

def code(request):
    code1 = request.session['code1']
    print(code1)
    form = TeleCodeForm
    if request.method == 'POST':
        telecode = request.POST.get('telecode')
        data = {
                'telecode' : telecode
        }
        form = TeleCodeForm(data)
        print(code1, telecode)
        if form.is_valid():
            if code1 == telecode:
                img = images()
                model = TelegrammUser()
                s = request.session
                print(s.items())
                tgname = s.get('tgname')
                user = request.user
                chat_id = s.get('chat_id')
                model.telelogin = tgname
                model.user = user
                model.chat_id = chat_id
                model.save()
                url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Ваша%20учетная%20запись%20успешно%20активирована!')
                resp = requests.get(url)
                return render(request, 'tgwin.html')

            else:
                context = {'form':form}
                return render(request, 'inputcode.html', context)
        
    context = {'form':form}
    return render(request, 'inputcode.html', context)

@csrf_exempt
def Check(request):
    if request.method == "POST":
        img = images()
        data = json.loads(request.body.decode())
        chat_id = str(data['owner']['chat_id'])
        
        try:
            user = TelegrammUser.objects.get(chat_id=chat_id)
            url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Добрый%20день%20снова!')
            resp = requests.get(url)
            
        except Exception as e:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text='Активируй свою учетную запись!', url='127.0.0.1:8000/tg/'))
            keyboard = keyboard.to_json()
            url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['notknow'] + '&caption=Мы%20еще%20не%20знакомы%20' + "&reply_markup=" + keyboard)
            print(traceback.format_exc)
            resp = requests.get(url)

    
    return HttpResponse(chat_id)

def LoginTele(request):
    code1 = request.session['code1']
    form = TeleCodeForm
    print('pidoraska ebuchaya')
    if request.method == 'POST':
        telecode = request.POST.get('telecode')
        
        data = {
                    'telecode' : telecode
        }
        form = TeleCodeForm(data)
        if form.is_valid():
            if code1 == telecode:
                img = images()
                model = TelegrammUser()
                s = request.session
                print(s.items())
                chat_id = s.get('chat_id')
                print(chat_id)
                teleUser = TelegrammUser.objects.get(chat_id=chat_id)
                user = teleUser.user
                print(type(user))
                login(request, user)
                return HttpResponseRedirect('/main/product')
                
                #url = ('https://api.telegram.org/bot6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ/sendPhoto?chat_id=' + chat_id + '&photo=' + img['like'] + '&caption=Ваша%20учетная%20запись%20успешно%20активирована!')
                #resp = requests.get(url)
                return render(request, 'tgwin.html')

    return render(request, 'logintele.html', context={'form':form})

