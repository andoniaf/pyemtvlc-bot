#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Librerías
import telegram
import logging

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

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    logger.info("Bot Started")
    logger.info("Keys: %s" % KEYS)
    update.message.reply_text(WELCOME_MESSAGE)
