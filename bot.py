import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "سلام 💗 به ربات ناشناس نیکیتا خوش اومدی!\n"
        "پیامت رو بفرست تا ناشناس به صاحب ربات ارسال بشه."
    )

@bot.message_handler(func=lambda message: True)
def receive(message):
    bot.reply_to(
        message,
        "پیامت دریافت شد 💌 برای فعال شدن ارسال ناشناس، "
        "باید آیدی عددی صاحب ربات تنظیم بشه."
    )

bot.infinity_polling()
