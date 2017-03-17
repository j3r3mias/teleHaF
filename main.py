#!/usr/bin/env python
# -*- coding:utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from requests import get
from json import loads
from configparser import ConfigParser
from emoji import emojize

# Configurando o bot
config = ConfigParser()
config.read_file(open('config.ini'))

# Conectando para o telegram API
# Updater ler as inforamações no arquivo config.ini e dispatcher conecta comandos
up = Updater(token=config['DEFAULT']['token'])
dispatcher = up.dispatcher


def start(bot, update):
    """
        Mostra uma mensagem de boas-vindas e informações de ajuda sobre os comandos disponíveis.
    """
	
    #Mensagem inicial
    msg = "Salve hackudos. \n"
    msg += "O que você gostaria de fazer? \n"
    msg += "/ranking Listará o top 10 atual do hackaflag \n"
    msg += "/help Caso precise de ajuda"
	
    # Envia a mensagem
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def ranking(bot, update):
    # Request via get para ler os dados, e decodificar o json
    r = loads(get('https://hackaflag.com.br/premio_json.php').text)
    msg = emojize("Ranking :black_flag:", use_aliases=True)
    """
        Retorno do request listando o top 10 de times.
    """
    msg += '\n1° - Time: ' + str(r['1']['nome']) + ' | Score: ' + str(r['1']['score']) + emojize(' :1st_place_medal:', use_aliases=True) #adding emoji gold
    msg += '\n2° - Time: ' + str(r['2']['nome']) + ' | Score: ' + str(r['2']['score']) + emojize(' :2nd_place_medal:', use_aliases=True) #adding emoji silver
    msg += '\n3° - Time: ' + str(r['3']['nome']) + ' | Score: ' + str(r['3']['score']) + emojize(' :3rd_place_medal:', use_aliases=True) #adding emoji bronze
    msg += '\n4° - Time: ' + str(r['4']['nome']) + ' | Score: ' + str(r['4']['score'])
    msg += '\n5° - Time: ' + str(r['5']['nome']) + ' | Score: ' + str(r['5']['score'])
    msg += '\n6° - Time: ' + str(r['6']['nome']) + ' | Score: ' + str(r['6']['score'])
    msg += '\n7° - Time: ' + str(r['7']['nome']) + ' | Score: ' + str(r['7']['score'])
    msg += '\n8° - Time: ' + str(r['8']['nome']) + ' | Score: ' + str(r['8']['score'])
    msg += '\n9° - Time: ' + str(r['9']['nome']) + ' |Score: ' + str(r['9']['score'])
    msg += '\n10° - Time: ' + str(r['10']['nome']) + ' | Score: ' + str(r['10']['score'])

    # Envia a mensagem
    bot.send_message(chat_id=update.message.chat_id,text=msg)


def help(bot, update):
    """
	    Mostra uma descrição sobre o bot e suas funções
    """

    # Mensagem de ajuda
    msg = "Olá, sou um bot que lhe ajudará com algumas \n"
    msg += "informações sobre o hackaflag 2017. \n"
    msg += "Atualmente conto com apenas uma função, \n"
    msg += "/ranking, essa função listará o top 10, \n"
    msg += "de times do hackaflag 2017."
	
    # Envia a mensagem
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def unknown(bot, update):
    """
        Caso o usuário envie um comando desconhecido.
    """
    msg = "Digite uma função valida!."
	
	# Envia a mensagem
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

# Adicionando os handlers start, ranking, help e unknown
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('ranking', ranking))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler((Filters.command), unknown))

up.start_polling() # Inicia o progama
print(":)")
