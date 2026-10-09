import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN sozlanmagan!")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "🤖 Fragment Alerts Demo Bot\n\n"
        "Bu faqat sinov uchun yaratilgan bot.\n"
        "Haqiqiy auktsionlar yoki takliflarni "
        "kuzatmaydi.\n\n"
        "Buyruqlar:\n"
        "/demo - sinov alerti\n"
        "/help - yordam"
    )
    bot.reply_to(message, text)


@bot.message_handler(commands=["demo"])
def demo(message):
    text = (
        "🔔 DEMO ALERT\n\n"
        "📦 Sinov taklifi\n"
        "💎 Narx: 100 TON (demo)\n\n"
        "⚠️ Bu soxta sinov ma'lumoti.\n"
        "Haqiqiy Fragment taklifi emas."
    )
    bot.reply_to(message, text)


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "Yordam:\n"
        "/start - botni boshlash\n"
        "/demo - sinov xabarini olish"
    )


@bot.message_handler(func=lambda message: True)
def other_messages(message):
    bot.reply_to(
        message,
        "Buyruqni tanlang:\n"
        "/start\n"
        "/demo\n"
        "/help"
    )


print("Demo bot ishga tushdi!")
bot.infinity_polling(skip_pending=True)
