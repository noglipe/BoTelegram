import os

def validarUsuario(mensagem):
    print("Validando Usuário " + mensagem.from_user.username)

    if mensagem.from_user.username in os.environ['lista']:
        return True
    else:
        return False
