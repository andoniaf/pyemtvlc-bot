#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Librerías
import telegram
import logging
import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters
from settings import TOKEN, USERS, LOGLEVEL

# Vars
WELCOME_MSG = 'Bot iniciado y listo para servir!'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.LOGLEVEL)

logger = logging.getLogger(__name__)


def main():
    print("Starting bot!")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add your other handlers here...
    def start(update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text=WELCOME_MSG)

    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@xTrece')))

    # Start the Bot start_polling() method
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
