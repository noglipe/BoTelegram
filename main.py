import os

import telebot
from time import sleep

from Tools.acessoBinance import ConsultaBinance
from Tools.bibliaConsulta import BibliaOnline
from Tools.img_to_text import converter

bot = telebot.TeleBot(os.environ['CHAVE_API'])
print("ChatBot Iniciado")


@bot.message_handler(commands=["preço", "preco"])
def consultarPreco(mensagem):
    print("Consultando Valor Cripto!")
    moeda = mensagem.text[7:].upper()
    if len(moeda) > 0:
        cripto = ConsultaBinance(moeda)
        bot.send_message(mensagem.chat.id, cripto.consultarValor(), parse_mode='Markdown')
    else:
        bot.send_message(mensagem, 'Nenhuma Moeda Informada')

@bot.message_handler(commands=["va"])
def verciculoAleatorio(mensagem):
    biblia = BibliaOnline
    biblia.verciculoAleatorio()
    bot.send_message(mensagem.chat.id, biblia.dados)


@bot.message_handler(commands=["v"])
def verciculo(mensagem):
    biblia = BibliaOnline()
    biblia.verciculo(mensagem)
    bot.send_message(mensagem.chat.id, biblia.dados)


def verificar(mensagem):
    print(mensagem.chat)
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    #bot.send_message(mensagem.chat.id,
     #                mensagem.from_user.first_name + " Bem vindo! \nPara maiores informações acesse:\nhttps://github.com/noglipe/BoTelegram")
    print(mensagem)


def processPhotoMessage(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file = bot.get_file(fileID)
    print ('file.file_path =', file.file_path)

@bot.message_handler(content_types= ["photo"])
def fotoPtexto(message):
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file = bot.download_file(file_path)
    sleep(5)

    with open('image.jpg', 'wb') as new_file:
        new_file.write(file)

    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, converter())



# LoopInolfinito
bot.polling()
