# -*- coding: utf-8 -*-
import json
import urllib.request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from urllib.parse import quote

updater = Updater(token='611183616:AAHttgu-yVWO-voWaGlMRTUNgTyX9m3BstE')
dispatcher = updater.dispatcher
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
key = 'key=trnsl.1.1.20181009T093624Z.bbb44dfc43821e97.b4a9a4330fc84e5d33031378f026afb018e30492'
language = 'lang=en'

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Введите текст для перевода')
def textMessage(bot, update):
    text = update.message.text
    req = url+'?'+key+'&'+'text='+format(quote(text))+'&'+language
    response = urllib.request.urlopen(req)
    data = response.read()
    encoding = response.info().get_content_charset('utf-8')
    response_json = json.loads(data.decode(encoding))
    translate = response_json['text'][0]
    result = 'Перевод: ' + translate
    bot.send_message(chat_id=update.message.chat_id, text=result)

start_command_handler = CommandHandler('start', startCommand)
message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(message_handler)
updater.start_polling(clean=True)
updater.idle()