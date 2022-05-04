import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("Hello, welcome to my first bot!")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start --- starts the bot
    /help --- this exact message
    """)

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))

updater.start_polling()
updater.idle()

