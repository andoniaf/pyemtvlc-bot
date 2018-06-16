#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Librerías
import telebot
from telebot import types # Tipos para la API del bot.
from datetime import datetime
import time # Librería para hacer que el programa que controla el bot no se acabe.
from modules.uptime import uptime_string
from modules.uptime import logs_size
# Importamos el TOKEN y USERS desde settings
from settings import TOKEN
from settings import USERS
from vars import LOGDIR
from vars import LOGFILE
from vars import path
#Modulo EMT VLC
from modules.emtVlc import prime_buses
import os

bot = telebot.TeleBot(TOKEN) # Creamos el objeto del bot.
print("Bot iniciado y listo para servir:")
############ VARS #######################
start_time = time.time()
last_error_time = None
#########################################
test_menu = types.ReplyKeyboardMarkup()
test_menu.add("/emt 764", "/emt 1547")

############ LISTENER ###################
# Con esto, estamos definiendo una función llamada 'listener', que recibe como
#   parámetro un dato llamado 'messages'.
def listener(messages):
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            if cid > 0:
                # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
                mensaje = "[" + now + "]: " + str(m.chat.first_name) + "(" + str(cid) + "): " + m.text
            else:
                # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
                mensaje = "[" + now + "]: " + str(m.from_user.first_name) + "(" + str(cid) + "): " + m.text
            f = open( LOGDIR + LOGFILE, 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
            f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
            f.close() # Cerramos el fichero para que se guarde.
            #mensaje = update.mensaje.text.encode('utf-8')
            print(mensaje) # Imprimimos el mensaje tambien en la terminal

# Ejecutamos funcion que "escucha" los mensajes
bot.set_update_listener(listener)
#########################################
############ FUNCIONES ##################
##### Comandos publicos #####
## Funciona basica de testeo
@bot.message_handler(commands=['helloworld']) # comando '/helloworld'
def command_helloworld(m): # Definimos la función
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    # funcion 'send_message()' del bot: enviamos al ID de chat guardado el texto indicado
    bot.send_message( cid, 'Hello World')

## Funcion de prueba para controlar que usuarios pueden usar los comandos BOT
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    # Si no esta en la lista de chats permitidos, deniega acceso
    if not str(cid) in USERS:
        bot.send_message( cid, "Permiso denegado")
    else:
        bot.send_message( cid, "Permiso concedido")

@bot.message_handler(commands=['windows']) # comando '/windows'
def command_windows(m): # Definimos la función
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    # Si no esta en la lista de chats permitidos, deniega acceso
    if not str(cid) in USERS:
        bot.send_message( cid, "Permiso denegado, aunque igualmente Windows mola menos que Linux")
    else:
        bot.send_message( cid, 'Windows mola menos que Linux')

# Comando que muestra enlace al blog
@bot.message_handler(commands=['blog'])
def command_repo(m):
    markup = types.InlineKeyboardMarkup()
    itembtnrepo = types.InlineKeyboardButton('Pulsar aqui!', url='https://andoniaf.github.io/')
    markup.row(itembtnrepo)
    bot.send_message(m.chat.id, '\U000021b3 Blog Nº13:', reply_markup=markup)

# Muestra el uptime del servidor
@bot.message_handler(commands=['uptime'])
def command_uptime(m):
    cid = m.chat.id
    bot.send_chat_action(cid, "typing")
    message = uptime_string(start_time, last_error_time)
    bot.send_message(cid, message)

@bot.message_handler(commands=['emt'])
def command_emt(m):
    cid = m.chat.id
    bot.send_chat_action(cid, "typing")
    parada = m.text.strip('/emt ')
    # Comprobar si se ha introducido una parada "valida"
    if parada == '':
        message = "No has introducido la parada!!"
    elif parada.isdigit() != True:
        message = "No has introducido un numero de parada valido."
    else:
        message = prime_buses(parada)
    bot.send_message(cid, message)

### Testing EMT
@bot.message_handler(commands=['bus'])
def command_bus(m):
    cid = m.chat.id
    bot.send_message(cid, "Wake up " + str(m.chat.first_name) + "...")
    time.sleep(1)
    bot.send_message(cid, "Menu EMT:\n", reply_markup=test_menu)

###############
##### Comandos reservados #####
@bot.message_handler(commands=['logsize'])
def command_logsize(m):
    cid = m.chat.id
    if not str(cid) in USERS:
        bot.send_message( cid, "Permiso denegado")
    else:
        bot.send_chat_action(cid, "typing")
        message = logs_size(path)
        bot.send_message(cid, message)

#########################################
# Con esto, le decimos al bot que siga funcionando incluso si encuentra
#   algún fallo.
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        last_error_time = time.time()
