from telebot import types
from bot import bot
from database.session import SessionLocal
from database.crud import get_or_create_user


db = SessionLocal()

@bot.message_handler(command=["start"])
def start_handler(message):
    
    try :
        user = get_or_create_user(
            db, 
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.username
        )
        bot.reply_to(
            message,
             f"سلام {user.first_name} 👋\n"
            "به ربات دانلود کنار خوش اومدی 🎵",
            )
    finally:
        db.close()