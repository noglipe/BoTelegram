import requests

class BibliaOnline:

    versao = 'nvi'
    idioma = 'pt'
    urlVerciculo = 'https://www.abibliadigital.com.br/api/verses/'  #:version/:abbrev/:chapter/:number
    livro = ''
    capitulo = ''
    verciculo = ''
    dados = ''
    status = ''

    livros = ['gn', 'ex', 'lv', 'nm', 'dt', 'js', 'jz', 'rt', '1sm', '2sm', '1rs', '2rs', '1cr', '2cr', 'ed', 'ne', 'et', 'job', 'sl', 'pv', 'ec', 'ct', 'is', 'jr', 'lm', 'ez', 'dn', 'os', 'jl', 'am', 'ob', 'jn', 'mq', 'na', 'hc', 'sf', 'ag', 'zc', 'ml', 'mt', 'mc', 'lc', 'jo', 'at', 'rm', '1co', '2co', 'gl', 'ef', 'fp', 'cl', '1ts', '2ts', '1tm','2tm','tt', 'fm', 'hb', 'tg', '1pe', '2pe', '1jo', '2jo', '3jo', 'jd', 'ap']

    #def __init__(self):

    @classmethod
    def verciculoAleatorio(self):
        url = f'{self.urlVerciculo}{self.versao}/{self.idioma}/random'

        print(url)
        requisicao = requests.get(url)

        print(requisicao)
        js = requisicao.json()

        if requisicao.status_code == 200:
            self.dados = f'{js["text"]} {js["book"]["name"]}: {js["chapter"]}:{js["number"]}'
        else:
            self.dados = js["msg"]


    def endereco(self, listaEnd):
        self.livro = listaEnd[0]
        self.capitulo = listaEnd[1]
        self.verciculo = listaEnd[2]


    def verciculo(self, mensagem):
        lista = mensagem.text[3:].lower().split(".")
        print(lista)
        self.livro = lista[0]
        self.capitulo = lista[1]

        if self.livro in self.livros:
            url = f'{self.urlVerciculo}{self.versao}/{self.livro}/{self.capitulo}'
            print(url)
            requisicao = requests.get(url)
            print(requisicao)
            js = requisicao.json()

            if len(lista) != 3:
                if len(lista) > 3:
                    if int(lista[3]) > int(js["chapter"]["verses"]):
                        self.dados = f"Número Máximo de Vercículos {js['chapter']['verses']}"
                    minimo = int(lista[2])
                    maximo = int(lista[3])
                else:
                    minimo = 1
                    maximo = int(js["chapter"]["verses"])

                self.dados = ''
                print(js["verses"])
                for verso in js["verses"]:
                    if (int(verso["number"]) >= minimo) and (int(verso["number"]) <= maximo):
                        self.dados = self.dados + " " + verso["text"]
                self.dados = self.dados + F" - {js['book']['name']} : {minimo}-{maximo}"

                if len(self.dados) > 4096:
                    self.dados = "Tamanho de texto não suportado"

            if len(lista) == 3:
                self.endereco(lista)
                url = f'{self.urlVerciculo}{self.versao}/{self.livro}/{self.capitulo}/{self.verciculo}'
                requisicao = requests.get(url)
                print(requisicao)
                js = requisicao.json()
                if requisicao.status_code == 200:
                    self.dados = f'{js["text"]} {js["book"]["name"]}: {js["chapter"]}:{js["number"]}'
                else:
                    self.dados = js["msg"]
