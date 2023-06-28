from config import TOKEN
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет, я бот-органайзер, я помогу тебе сделать тайм-менеджмент удобнее')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


