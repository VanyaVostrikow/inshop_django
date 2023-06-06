import telebot
from writeuser import create_db
import os
import time
from telebot import types
from collections import defaultdict
from JsonGET import Get
from JsonPOST import PostOrder, PostCoupon, PostCheck
from JSON import Create
import json
import requests
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import pathlib
import shutil
from datetime import datetime
token='6132473598:AAF1FMmD4ofoum9nIkLBfULPMwdBebCV_kQ'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    folder_id = str(chat_id)
    data = {'chat_id':chat_id}
    if os.path.exists(f"crate/users/{chat_id}"):
         print("V")
         print(message)
    else:
        print("X")
        os.mkdir(f'crate/users/{chat_id}')
        os.mkdir(f'crate/users/{chat_id}/DB')
        os.mkdir(f'crate/users/{chat_id}/logs')
        dst = f'crate/users/{chat_id}/DB'
        src = 'crate/DB/tg_DB.sqlite3'
        log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
        log_file.write(f"{datetime.now()}-----------!Created Log File!--------------\n")
        
        log_file.close()
        shutil.copy2(src, dst)
        print(message)
        create_db(chat_id, message.chat.first_name, message.chat.last_name, message.chat.username)
    PostCheck(data)

@bot.message_handler(commands=['button'])
def button_message(message):
    chat_id = message.chat.id
    log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
    log_file.write(f"{datetime.now()}-----------!TapButton!--------------\n")
    log_file.close()

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3=types.KeyboardButton("🚩Получить купон🚩")
    item2=types.KeyboardButton("⚽⚾Выиграй купон⚽⚾")
    item1=types.KeyboardButton("🔺🐔🔻Наш сайт🔺🐔🔻")
    item6=types.KeyboardButton("⚽⚾Мой заказ⚽⚾")
    item4=types.KeyboardButton("🔺🐔🔻Активировать аккаунт CPUshop🔺🐔🔻")
    item5=types.KeyboardButton("🔺🔻ТЕСТ АПИ🔺🔻")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="🔺🔻ТЕСТ АПИ🔺🔻":
        chat_id = message.chat.id
        data = {'chat_id': chat_id}
        resp = requests.get('http://127.0.0.1:8000/api/coupon', data)
        print(resp.text)
         
    if message.text=="🔺🐔🔻Наш сайт🔺🐔🔻":
        bot.send_message(message.chat.id,"http://127.0.0.1:8000/")
        chat_id = message.chat.id
        log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', "a")
        log_file.write(f"{datetime.now()}-----------!View Site Address!--------------\n")
        log_file.close()

    if message.text=="⚽⚾Мой заказ⚽⚾":
            #sent = bot.send_message(message.chat.id, 'Поиск...')
            photo = open('search.jpg', 'rb')
            sent = bot.send_photo(message.chat.id, photo, 'Уже ищу ваш заказ')
            chat_id = (sent.__dict__['json']['chat']['id'])

            try:
                log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', "a")
            except:
                os.mkdir(f'crate/users/{chat_id}')
                os.mkdir(f'crate/users/{chat_id}/DB')
                os.mkdir(f'crate/users/{chat_id}/logs')
                dst = f'crate/users/{chat_id}/DB'
                src = 'crate/DB/tg_DB.sqlite3'
                log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
                log_file.write(f"{datetime.now()}-----------!Created Log File!--------------\n")
                log_file.close()
                shutil.copy2(src, dst)

            log_file.write(f"{datetime.now()}-----------!Search Order!--------------\n")
            log_file.write(f"{datetime.now()}-----------!{sent}!--------------\n")

            time.sleep(2)
            chat_id = (sent.__dict__['json']['chat']['id'])
            data = {'chat_id':chat_id}

            log_file.write(f"{datetime.now()}-----------{data}--------------\n")
            print(chat_id)
            resp = PostOrder(data)

            log_file.write(f"{datetime.now()}-----------!{resp.headers}!--------------\n")
            log_file.close()


    if message.text=="🚩Получить купон🚩" or message.text=="Получить купон":
            
            photo = open('search.jpg', 'rb')
            sent = bot.send_photo(message.chat.id, photo, 'Ищу вот прям все ваши купоны...')

            time.sleep(2)
            #sent = bot.send_message(message.chat.id, 'Поиск...')
            chat_id = (sent.__dict__['json']['chat']['id'])
            data = {'chat_id':chat_id}

            try:
                log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', "a")
            except:
                os.mkdir(f'crate/users/{chat_id}')
                os.mkdir(f'crate/users/{chat_id}/DB')
                os.mkdir(f'crate/users/{chat_id}/logs')
                dst = f'crate/users/{chat_id}/DB'
                src = 'crate/DB/tg_DB.sqlite3'
                log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
                log_file.write(f"{datetime.now()}-----------!Created Log File!--------------\n")
                shutil.copy2(src, dst)

            log_file.write(f"{datetime.now()}-----------!Search Coupon!--------------\n")
            log_file.write(f"{datetime.now()}-----------!{sent}!--------------\n")

            print(chat_id)
            print(sent)
            resp = PostCoupon(data)
            log_file.write(f"{datetime.now()}-----------{data}--------------\n")
            print(type(sent))
            log_file.write(f"{datetime.now()}-----------!{resp.headers}!--------------\n")
            log_file.close()

    if message.text=="🔺🐔🔻Активировать аккаунт CPUshop🔺🐔🔻":
        sent = bot.send_message(message.chat.id,"Введите данный код по адресу http://127.0.0.1:8000/tg/: ")
        chat_id = message.chat.id
        try:
            log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', "a")
        except:
            os.mkdir(f'crate/users/{chat_id}')
            os.mkdir(f'crate/users/{chat_id}/DB')
            os.mkdir(f'crate/users/{chat_id}/logs')
            dst = f'crate/users/{chat_id}/DB'
            src = 'crate/DB/tg_DB.sqlite3'
            log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
            log_file.write(f"{datetime.now()}-----------!Created Log File!--------------\n")
            shutil.copy2(src, dst)

        log_file.write(f"{datetime.now()}-----------!Активировать аккаунт!--------------\n")

        text = message.text
        chat_id = (sent.__dict__['json']['chat']['id'])
        sent = bot.send_message(message.chat.id, chat_id)
        print(chat_id)
        print(text)
        print(type(sent))

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    chat_id = (callback.__dict__['json']['from']['id'])
    try:
        log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', "a")
    except:
        os.mkdir(f'crate/users/{chat_id}')
        os.mkdir(f'crate/users/{chat_id}/DB')
        os.mkdir(f'crate/users/{chat_id}/logs')
        dst = f'crate/users/{chat_id}/DB'
        src = 'crate/DB/tg_DB.sqlite3'
        log_file = open(f'crate/users/{chat_id}/logs/Log{chat_id}.txt', 'w+')
        log_file.write(f"{datetime.now()}-----------!Created Log File!--------------\n")
        shutil.copy2(src, dst)

    str_space = str(callback.__dict__['data'])    
    
    print(chat_id)
    list = str_space.split(' ')
    order_id = list[1]
    print(order_id)
    data = {'order_id' : order_id, 'chat_id': chat_id}
    url = 'http://127.0.0.1:8000/orders/searchbot/detail/'
    json_data = json.dumps(data)
    resp = requests.post(url, json=data)
    log_file.write(f"{datetime.now()}-----------{data}--------------\n")
    log_file.write(f"{datetime.now()}-----------!{resp.headers}!--------------\n")
    log_file.close()


bot.polling(none_stop=True, interval=0)
bot.infinity_polling()