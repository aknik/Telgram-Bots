# -*- coding: utf-8 -*-
# Basado en el trabajo original de https://github.com/i32ropie/Telgram-Bots/blob/master/ssh.py
# Cualquier comando precedido por / se envìa a la shell linux (bash) y todo lo demás
# a la sesión interactiva con Python. Excepto get:fihero que nos envia el fichero elegido.
# Estaba así en el original XDD

import telebot 
from telebot import types 
import time 
import subprocess 
import pexpect

TOKEN = "xxxxxxxxxxxxxtokendetubotxxxxxxxxxxxxxxxxxxx"
admin = 66ID666

bot = telebot.TeleBot(TOKEN) 

##################################################
c = pexpect.spawn ('/usr/bin/env python2')
c.expect(['>>>', pexpect.EOF, pexpect.TIMEOUT])
##################################################

def listener(messages):
    for m in messages:
        #print m
        if m.from_user.id == admin:
            if m.content_type == 'text':
                if m.text.startswith('get'):
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

        message.text = message.text[1:]
        #print message.text
        result_command = subprocess.Popen(message.text, shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
     
##################################################
    
		c.sendline(message.text)
		c.expect(['>>>', pexpect.EOF, pexpect.TIMEOUT])
    	result_command = c.before
    
##################################################


    print result_command
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
