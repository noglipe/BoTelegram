import os

import telebot

from Tools.acessoBinance import ConsultaBinance
from Tools.bibliaConsulta import BibliaOnline

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
    bot.send_message(mensagem.chat.id,
                     mensagem.from_user.first_name + " Bem vindo! \nPara maiores informações acesse:\nhttps://github.com/noglipe/BoTelegram")


# LoopInolfinito
bot.polling()
