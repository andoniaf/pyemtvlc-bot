#!/usr/bin/python3

# Librerías
import logging
import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters
from settings import TOKEN

from modules.utils import uptime_string, query_emt

# Vars
INIT_MSG = 'Bot iniciado y listo para servir!'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def main():
    print("Starting bot!")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Functions
    def start(update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=INIT_MSG)

    def stop_and_restart():
        """Gracefully stop the Updater & replace curr process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    def uptime(update, context):
        text = uptime_string()
        update.message.reply_text(text)

    def emt_info(update, context):
        msg = update.message.text
        args = msg.strip('/emt ')
        if args == "":
            text = 'Uso: /emt <Parada> [<Linea>]'
        else:
            text = query_emt(args)
        update.message.reply_text(text)

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@xTrece')))
    dp.add_handler(CommandHandler("uptime", uptime))
    dp.add_handler(CommandHandler("emt", emt_info))

    # Start the Bot start_polling() method
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
