
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 Fragment Alerts Demo Bot\n\n"
        "Bu faqat demo bot. Haqiqiy auktsion yoki "
        "to'lovlar amalga oshirilmaydi."
    )

@bot.message_handler(func=lambda message: True)
def demo(message):
    bot.reply_to(
        message,
        "🔔 DEMO ALERT\n\n"
        "Bu sinov xabari.\n"
        "Haqiqiy Fragment taklifi emas."
    )

bot.infinity_polling()
