import json
import telebot;
from telebot.types import  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton



bot = telebot.TeleBot('6132473598:AAGsdtLQnnygLEMdjXcXTzvRQMd-H5DyxU4')

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')

    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif 'pagination' in req[0]:
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']

        
    
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                           InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                           InlineKeyboardButton(text=f'Вперёд --->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))



@bot.message_handler(content_types=['text'])
def start(m):
    page = 1




if __name__ == '__main__':
    bot.polling(none_stop=True)

