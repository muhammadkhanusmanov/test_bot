from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler,ConversationHandler
from telegram import (
    Bot,Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,
    InlineKeyboardButton,ChatAdministratorRights,ParseMode, MenuButtonWebApp,WebAppInfo,InputFile
    )
import sqlite3

bot = Bot('5655855014:AAFgMvIpeQ4CSn9N-q547jvM5YL286vfrT4')

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
        SELECT * FROM Users WHERE chat_id = "{chat_id}"
        """
        b = cr.execute(command).fetchall()
        if not b:
            command = f"""
            INSERT INTO Users (chat_id) VALUES ("{chat_id}")
            """
            cr.execute(command)
            cnt.commit()
        command = f"""
        SELECT chat_id FROM Users WHERE id = {1}
        """
        channel = cr.execute(command).fetchone()[0]
        text = "Assalomu alaykum botga xush kelibsiz, botdan to'liq foydalanish uchun majburiy obunani bajaring."
        btn1 = InlineKeyboardButton('Obuna ➕',callback_data='obuna',url=f'https://t.me/{channel[1:]}')
        btn2 = InlineKeyboardButton('Tekshirish',callback_data='user obuna')
        btn = InlineKeyboardMarkup([[btn1],[btn2]])
    bot.sendMessage(chat_id,text,reply_markup=btn)

def check(chat_id,bot,channel):
    chan1=bot.getChatMember(channel,str(chat_id))['status']
    if chan1=='left':
        return False
    return True

def userfun(update:Update, context:CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    msg = query.message.message_id
    bot=context.bot
    b = query.data.split(' ')[1]
    cnt = sqlite3.connect('data.db')
    cr = cnt.cursor()
    command = f"""
     SELECT chat_id FROM Users WHERE id = {1}
    """
    channel = cr.execute(command).fetchone()[0]
    a = check(chat_id,bot,channel)
    bot.delete_message(chat_id,msg)
    if a:
        text = "Obuna mufavaqiyatli amalga oshirildi!\nBo'limlardan birini tanlang."
        btn1 = InlineKeyboardButton("Test yaratish",callback_data='test +')
        btn2 = InlineKeyboardButton("Test yechish",callback_data='test tek')
        btn = InlineKeyboardMarkup([[btn1,btn2]])
        bot.sendMessage(chat_id,text,reply_markup=btn)
    else:
        bot.sendMessage(chat_id,'Obuna bo\'lishda xatolik!')


