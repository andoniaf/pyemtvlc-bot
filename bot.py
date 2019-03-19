#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Librerías
import telebot
import time
from telebot import types  # Tipos para la API del bot.
from datetime import datetime
from modules.uptime import uptime_string, query_emt
# Importamos el TOKEN y USERS desde settings
from settings import TOKEN, USERS
from vars import LOGDIR, LOGFILE, path
import os


bot = telebot.TeleBot(TOKEN)  # Creamos el objeto del bot.
print("Bot iniciado y listo para servir:")
# ########### VARS #######################
start_time = time.time()
last_error_time = None
# ########################################
# test_menu = types.ReplyKeyboardMarkup()
# test_menu.add("/emt 764", "/emt 1547")


# ########### LISTENER ###################
# Con esto, estamos definiendo una función llamada 'listener', que recibe como
#   parámetro un dato llamado 'messages'.
def listener(messages):
    for m in messages:  # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text':  # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id  # Almacenaremos el ID de la conversación.
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            if cid > 0:
                # Si 'cid' es >0, usaremos 'm.chat.first_name' para el nombre.
                mensaje = "[" + now + "]: " + str(m.chat.first_name) + "(" + str(cid) + "): " + m.text
            else:
                # Si 'cid' es <0, usaremos 'm.from_user.first_name'.
                mensaje = "[" + now + "]: " + str(m.from_user.first_name) + \
                        "(" + str(cid) + "): " + m.text
            f = open(LOGDIR + LOGFILE, 'a')
            f.write(mensaje + "\n")
            f.close()
            mensaje = update.mensaje.text.encode('utf-8')
            print(mensaje)


# Ejecutamos funcion que "escucha" los mensajes
bot.set_update_listener(listener)


#########################################
# ########### FUNCIONES ##################
# #### Comandos publicos #####
# Funcion basica de testeo
@bot.message_handler(commands=['helloworld'])  # comando '/helloworld'
def command_helloworld(m):  # Definimos la función
    cid = m.chat.id  # Guardamos el ID de la conversación para poder responder.
    # funcion 'send_message()' del bot: enviamos al ID de chat guardado el texto indicado
    bot.send_message(cid, 'Hello World')


# Funcion de prueba para controlar que usuarios pueden usar los comandos BOT
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    # Si no esta en la lista de chats permitidos, deniega acceso
    if not str(cid) in USERS:
        bot.send_message(cid, "Permiso denegado")
    else:
        bot.send_message(cid, "Permiso concedido")


# Comando que muestra enlace al blog
@bot.message_handler(commands=['blog'])
def command_repo(m):
    markup = types.InlineKeyboardMarkup()
    itembtnrepo = types.InlineKeyboardButton('Pulsar aqui!', url='https://andoniaf.github.io/')
    markup.row(itembtnrepo)
    bot.send_message(m.chat.id, '\U000021b3 Blog Nº13:', reply_markup=markup)


@bot.message_handler(commands=['emt'])
def command_emt(m):
    cid = m.chat.id
    bot.send_chat_action(cid, "typing")
    parada = m.text.strip('/emt ')
    message = query_emt(parada)
    bot.send_message(cid, message)


# ## Testing EMT
@bot.message_handler(commands=['bus'])
def command_bus(m):
    cid = m.chat.id
    bot.send_message(cid, "Wake up " + str(m.chat.first_name) + "...")
    time.sleep(1)
    bot.send_message(cid, "Menu EMT:\n", reply_markup=test_menu)


#########################################
# #### Comandos privados #####
# Muestra el uptime del servidor
@bot.message_handler(commands=['uptime'])
def command_uptime(m):
    cid = m.chat.id
    bot.send_chat_action(cid, "typing")
    message = uptime_string(start_time, last_error_time)
    bot.send_message(cid, message)


#########################################
# Con esto, le decimos al bot que siga funcionando incluso si encuentra
#   algún fallo.
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        last_error_time = time.time()
