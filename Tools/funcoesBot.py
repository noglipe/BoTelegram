
def validarUsuario(mensagem):
    print("Validando Usuário " + mensagem.from_user.username)
    lista = ['lipeNogueira']
    if mensagem.from_user.username in lista:
        return True
    else:
        return False



