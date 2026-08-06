import telebot
from config import BOT_TOKEN


bot = telebot.TeleBot("BOT_TOKEN")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(skip_pending=True)