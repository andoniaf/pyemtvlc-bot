#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Librerías
import telegram
import logging
import sys
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

import time
from datetime import datetime
from modules.uptime import uptime_string, query_emt
# Importamos el TOKEN y USERS desde settings
from settings import TOKEN, USERS
from vars import LOGDIR, LOGFILE, path
import os


# Vars
WELCOME_MESSAGE = 'Bot iniciado y listo para servir:'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARN)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Add your other handlers here...

    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    # ...or here...

    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@xTrece')))

    # ...or here, depending on your preference :)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
#def start(bot, update):
#    logger.info("Bot Started")
#    logger.info("Keys: %s" % KEYS)
#    update.message.reply_text(WELCOME_MESSAGE)
