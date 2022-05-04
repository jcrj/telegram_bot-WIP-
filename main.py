import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("Hello, welcome to my first bot!")

def stock(update, context):
    ticker = context.args[0] #args passed to the stock command eg. /stock AAPL (assumes user passes something valid)
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f'The current price of {ticker} is ${price:.2f}.')


def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start --- starts the bot
    /help --- this exact message
    /stock --- find latest price of XXX stock
    """)

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))

updater.start_polling()
updater.idle()

