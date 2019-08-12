import telebot
import pyowm
#Расписание
# import requests
# from bs4 import BeautifulSoup
# import re
# import datetime
#Расписание


bot = telebot.TeleBot("884504936:AAHd4fniaMcI88sj9cy9MiO51d4fAOBa2to")
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')  # You MUST provide a valid API key
observation = owm.weather_at_place('Уфа')
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]




#@bot.message_handler(content_types=['text'])
#def send_echo(message):
	# bot.reply_to(message, "Howdy, how are you doing?")
	#bot.send_message(message.chat.id, "Температура: "+str(temp)+"℃")

@bot.message_handler(commands=['pogoda'])
def send_echo(message):
	bot.send_message(message.chat.id, "Темпер11атура: "+str(temp)+"℃")




#Расписание

bot.polling( none_stop = True )