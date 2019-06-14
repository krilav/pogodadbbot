#pogodadbbot.py

import telebot
import pyowm
import math
import time

owm = pyowm.OWM('7215c81c62b322b41e0aa0eb1843c5d4', language = 'ru')

from telebot import apihelper

port = '7777'  
usernameProxy = 'tg-id415061327'
passwordProxy = '7XJ6DenC'
addressProxy = '@socksy.seriyps.ru'

apihelper.proxy = {'https':'socks5://' + usernameProxy + ':' + passwordProxy + addressProxy + ':' + port}

TOKEN = "842039603:AAFy4Cd_mWZSyjFEQGcUgI0uYP87ZrQy1pQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])

def send_echo(message):

	try:
		observation = owm.weather_at_place(message.text)

		w = observation.get_weather()
		temp = math.ceil( w.get_temperature('celsius')['temp'] )
		speed = w.get_wind()['speed']
		humidity = w.get_humidity()
		city_time = w.get_reference_time()
		sky = w.get_detailed_status()

		answer = 'Температура в городе ' + message.text + ' сейчас ' + str( temp ) + ' градус C' + '\n'
		answer += 'Влажность воздуха ' + str( humidity ) + '%' + '\n' 
		answer += 'Скорость ветра в городе ' + message.text + ' сейчас ' + str( speed ) + " м/с" + '\n'
		answer += 'На небе ' + sky + '\n'
		answer += 'Время - ' + str( time.ctime( city_time ) ) + '\n'

		bot.send_message(message.chat.id, answer)

	except:
		 bot.send_message(message.chat.id, 'Не верный город')


	

bot.polling( none_stop = True )



