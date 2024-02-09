from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler,ConversationHandler
from telegram import (
    Bot,Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,
    InlineKeyboardButton,ChatAdministratorRights,ParseMode, MenuButtonWebApp,WebAppInfo,InputFile
    )
import sqlite3

def start(update:Update, context:CallbackContext):
    cnt = sqlite3.connect('data.db')
    cr = cnt.cursor()
    bot=context.bot
    chat_id = update.message.chat_id
    command = f"""
        SELECT * FROM Admins WHERE chat_id = "{chat_id}"
    """
    a=cr.execute(command).fetchall()
    if a:
        text = "Assalomu alaykum botga xush kelibsiz, bo'limlardan birini tanlang."
        btn1 = InlineKeyboardButton('Statistika',callback_data=f'admin stc')
        btn2 = InlineKeyboardButton('Admin⚙️',callback_data='admin stng')
        btn3 = InlineKeyboardButton('Majburiy obuna',callback_data='admin obuna')
        btn4 = InlineKeyboardButton('Xabar yuborish',callback_data='admin msg')
        btn = InlineKeyboardMarkup([[btn2,btn1], [btn3,btn4]])
    else:
        command = f"""
        SELECT chat_id FROM Users WHERE id = {1}
        """
        channel = cr.execute(command)[0]
        text = "Assalomu alaykum botga xush kelibsiz, botdan to'liq foydalanish uchun majburiy obunani bajaring."
        btn1 = InlineKeyboardButton('Obuna ➕',callback_data='obuna',url=f'https://t.me/{channel[1:]}')
        btn2 = InlineKeyboardButton('Tekshirish',callback_data='user obuna')
        btn = InlineKeyboardMarkup([[btn1],[btn2]])
    bot.sendMessage(chat_id,text,reply_markup=btn)