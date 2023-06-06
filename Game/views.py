from django.shortcuts import render, redirect
from .App import insert, answer, check
from django.conf import settings
from .forms import GameForm
from random import randint
from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
import django.middleware.csrf
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_csrf(request):
    csrf = django.middleware.csrf.get_token(request)
    print(csrf)
    return Response({"result": csrf}, status=status.HTTP_200_OK)


def StartGame(request):
 
    ans = answer()
    Ntry = 4
    ansbox = list()
    request.session['ansbox'] = ansbox
    request.session['ans'] = ans
    request.session['Ntry'] = Ntry

    return render(request, 'startgame.html')


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_out(request):
    data = request.data
    var1_list = insert(data['input'])
    var1 = data['input']
    s = request.session
    Ntry = s['Ntry']
    ans = s['ans']
    result = check(ans, var1)
    request.session['Ntry'] = Ntry - 1
    place = result[0]
    all = result[1]
    print(Ntry)  
    return Response({"result": var1, 'place':place, 'all':all, 'Ntry':Ntry}, status=status.HTTP_200_OK)

def win(request):
    text = "check ur telegramm for coupon!"
    return render(request, 'win.html', {'text':text})




def BNC(request: HttpRequest):
    ####    VARS
    place = 0
    all = 0
    s = request.session     #присваиваем сессионый запрос

    ans = s.get('ans')      #вытаскиваем ответ
    print(ans)
    ansbox = s.get('ansbox')
    Ntry = s.get('Ntry')    #вытаскиваем попытки
    print(Ntry)


    
    text = "Play to BnC and get a cupon to 20% SALE!"
    

    if request.method == 'POST':
        if Ntry > 1:
            Ntry = Ntry - 1                          ### увеличиваем счетчик
            request.session['Ntry'] = Ntry          ### присваиваем в сессию счетчик
            s = request.session 
            
            var1 = request.POST.get('input')
            user = request.user
            data = {'input': var1}
            print(data)
            form = GameForm(data)
            if form.is_valid():
                var1 = insert(var1)
                result = check(ans, var1)
                place = result[0]
                all = result[1]
                game = {'var1':var1,
                        'place':place,
                        'all':all,}
                ansbox.append(game)

                for i in range(len(ansbox)):
                    a = ansbox[i]
                    print(a)
                    
                ansbox[9-Ntry]
                if result == [4, 4]:
                    Ntry = str(Ntry)
                    user = request.user.username
                    #print(s.items())
                    hash = s.get('_auth_user_hash')[:5]
                    text = "check ur telegramm for coupon!"
                    return render(request, 'win.html', {'text':text})
            else:
                error = 'INCORRECT'
        else:
            text = "SOSI UEBISHE LOL"
            
            print(text)
            return render(request, 'gameover.html')
    form = GameForm
    context = {
        'text' : text,
        'form' : form,
        'ans' : ans,
        'Ntry': Ntry,
        'Place': place,
        'All': all,
        }
    return render(request, 'game.html', context)