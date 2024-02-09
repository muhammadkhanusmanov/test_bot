from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler,ConversationHandler
from mainfuncs import (
    start
)


updater=Updater('5655855014:AAFgMvIpeQ4CSn9N-q547jvM5YL286vfrT4')

dp = updater.dispatcher
dp.add_handler(CommandHandler('start',start))


updater.start_polling()
updater.idle()