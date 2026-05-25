from bot import bot
from keep_alive import keep_alive
import os

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
