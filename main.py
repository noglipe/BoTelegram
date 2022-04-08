import os
import telebot
import os
from Tools.funcoesBot import validarUsuario
#from chave_api import CHAVE_API
from Tools.acessoBinance import ConsultaBinance
from Tools.bibliaConsulta import BibliaOnline

bot = telebot.TeleBot(os.environ['CHAVE_API'])

@bot.message_handler(commands=["preço", "preco"])
def consultarpreco(mensagem):
    if validarUsuario(mensagem):
        moeda = mensagem.text[7:].upper()
        consulta = ConsultaBinance(moeda)
        valor = consulta.consultarValor()
        if valor == "Erro":
            bot.send_message(mensagem.chat.id, "Erro ao realizar consulta!\nFavor Verificar o código da moeda!")
        else:
            bot.send_message(mensagem.chat.id, f"*Moeda:* {moeda} \n*R$:* {valor}", parse_mode='Markdown')
    else:
        bot.send_message(mensagem.chat.id, "Usuário não autenticado!")


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
    bot.send_message(mensagem.chat.id, mensagem.from_user.first_name + " Bem vindo! Este é um robo Privado! \nAlgumas funções podem não funcionar se você não estiver cadastrado na plataforma!")

#LoopInolfinito
bot.polling()