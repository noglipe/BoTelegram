# <p align="center">botTelegram
# <p align="center"><a href="https://t.me/TestesLipe_bot">@TestesLipe_bot</a>

<p align="center"> Um robo em python onde estou implementando algumas funções com o intuito de aprendizado e praticar a linguagem. É um chatBot em construção sem um fim específico.</p>

<p align="center">FASE ATUAL: <strong>Refatorando o Código</strong></p>


## Início
O chatbot possui duas ferramentas implementadas no momento:

* Valor de Criptomoeda
* Bíblia

### CRIPTOMOEDA

Estou utilizando a API da Binance para fazer a requisição e pegar o preço da moeda desejada

#### CRIPTOMOEDA — Funções Implementadas

Consulta de Valor:
```bash
/preco btc
```
ou
```bash
/preço btc
```
É necessário informar a abreviação da moeda na binance.
O valor sempre é retornado em Real (R$)

### Bíblia

Estou utilizando a API <a href="https://github.com/marciovsena/abibliadigital">A Bíblia Digital</a>
No momento a versão utilizada é a NVI por padrão.

#### Bíblia — Funções Implementadas

#### Versículo Aleatório
```bash
/va
```
#### Consulta de Versículos e Capítulos

Para consultar versículos eu posso passar buscar por um versículo específico, um conjunto de versículos e um capítulo inteiro
Os parâmetros da pesquisa deve ser separados por um "."
Funciona indiferente se as letras foram maiúsculas ou minúsculas

##### Versículo Específico
```bash
/v jo.3.19
# Livro.Capitulo.Versículo
# Retorna João 3:16
```

##### Conjunto de Versículos
```bash
/v jo.3.16.17
# Livro.Capitulo.VersículoInicio.VersículoFinal
# Retorna João 3:16-17
```

##### Capítulo Inteiro
```bash
/v jo.3
# Livro.Capitulo
# Retorna João 3
```