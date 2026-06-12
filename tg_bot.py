import telebot
from telebot import types

TOKEN = "8960732780:AAGNm8fXms6EdtaN4f3Y40q46EnLGZKCaTE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📋 Мои услуги")
    btn2 = types.KeyboardButton("💰 Цены")
    btn3 = types.KeyboardButton("📞 Контакты")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, 
        "Привет! Я бот-визитка разработчика taoroa.\nВыбери раздел 👇",
        reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📋 Мои услуги")
def services(message):
    bot.send_message(message.chat.id,
        "🛠 Мои услуги:\n\n"
        "• Telegram-боты\n"
        "• Парсеры сайтов\n"
        "• Автоматизация задач\n"
        "• Google Sheets интеграции\n"
        "• Python скрипты под заказ")

@bot.message_handler(func=lambda m: m.text == "💰 Цены")
def prices(message):
    bot.send_message(message.chat.id,
        "💰 Стоимость работ:\n\n"
        "• Простой бот — от 1000 ₽\n"
        "• Парсер сайта — от 500 ₽\n"
        "• Скрипт автоматизации — от 1000 ₽\n"
        "• Сложные проекты — по договорённости")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def contacts(message):
    bot.send_message(message.chat.id,
        "📞 Связаться со мной:\n\n"
        "Telegram: @taoroa01\n"
        "kwork: https://kwork.ru/user/taoroa01\n"
        "GitHub: https://github.com/taoroa12")
        

bot.polling()