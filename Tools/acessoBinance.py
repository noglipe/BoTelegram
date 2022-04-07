import requests

class ConsultaBinance:

    def __init__(self, cryptoConsulta, moedaRetorno='BRL'):
        self.moedaRetorno = moedaRetorno
        self.cryptoConsulta = cryptoConsulta

    def consultarValor(self):

        codigo = self.cryptoConsulta + self.moedaRetorno
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={codigo}"
        requisicao = requests.get(url)

        if requisicao.status_code == 400:
            return "Erro"
        else:
            dados = requisicao.json()
            return dados['price']