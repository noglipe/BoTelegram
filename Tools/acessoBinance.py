import requests


class ConsultaBinance:
    urlbase = "https://api.binance.com/api/v3/ticker/price?symbol="
    moedaParaRetorno = ''
    criptoParaConsulta = ''
    simboloMoeda = ''

    def __init__(self, criptoParaConsulta, moedaParaRetorno='BRL', simboloMoeda='R$'):
        self.moedaParaRetorno = moedaParaRetorno
        self.criptoParaConsulta = criptoParaConsulta
        self.simboloMoeda = simboloMoeda

    def consultarValor(self):
        url = f"{self.urlbase}{self.criptoParaConsulta}{self.moedaParaRetorno}"
        requisicao = requests.get(url)

        if requisicao.status_code == 400:
            return "Erro ao realizar consulta!\nFavor Verificar o código da moeda!"
        else:
            dados = requisicao.json()
            return f"*Moeda:* {dados['symbol']} \n*R$:* {dados['price']}"
