
# -*- coding: utf-8 -*-
import telebot 
from telebot import types 
import time 
import subprocess 

TOKEN = "-------------------------------"
admin = 6660666
bot = telebot.TeleBot(TOKEN) 

def listener(messages):
    for m in messages:
        #print m
        if m.from_user.id == admin:
            if m.content_type == 'text':
                if m.text.startswith('get'):
                    # Si el comando empieza por get , envia el fichero indicado get:fichero 
                    pwd = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE).stdout.read()
                    pwd = pwd[0:len(pwd)-1]
                    try:
                        bot.send_document( admin, open( pwd + '/' + m.text.split(':')[1] ) )
                    except:
                        bot.send_message( admin, "Error enviando el documento")
                else:
                    execute_command(m)
                print str(m.from_user.first_name) + " [" + str(m.chat.id) + "]: " + m.text 

bot.set_update_listener(listener) 

def execute_command(message):
    cid = message.chat.id
    
    if message.text.startswith('/'):
        # Si el texto empieza por / lo considera comando bash y en caso contrario, python
        message.text = message.text[1:]
        print message.text
    else:
        # Se le envia el comando como instruccion a calcular en python
        message.text = "python2 -c 'from math import *; print " + message.text + "'" 
    
    result_command = subprocess.Popen(message.text, shell=True, stdout=subprocess.PIPE).stdout.read()
#    print result_command
    try:
        bot.send_message( cid, result_command)
    except:
        exception = True
    else:
        exception = False
    
    if exception:
        if result_command == "":
            bot.send_message( cid, "?")
        else:
            with open( 'tmp.txt', 'w') as f:
                f.write( result_command)
            bot.send_document( cid, open( 'tmp.txt', 'rb'))
bot.polling(none_stop=True)

	
