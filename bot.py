import telebot
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(os.environ.get('TG_TOKEN'))

@bot.message_handler(func=lambda message: True)
def handle(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)
