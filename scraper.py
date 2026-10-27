#Vai buscar/ trazer as vagas com auxílio dos requests.get

import requests

#Endereço da API que vai direto para o repositório das vagas 
URL = "https://api.github.com/repos/backend-br/vagas/issues"

#Teste com 3 vagas abertas
parametros = {"state": "open", "per_page": 3}

#Realiza a identificação de quem está pedindo os dados
cabecalhos = {"User-Agent": "bot-vagas-estudo/0.1 (projeto pessoal)"}

#Faz o pedido , caso passe de 10 segundos ele desiste 
resposta = requests.get(URL, params=parametros, headers=cabecalhos, timeout=10)

print(resposta.status_code)   #Retorna 200 que deu certo
vagas = resposta.json()       #Lista as vagas
print(len(vagas))             #Quantidade de vagas que vieram 
print(vagas[0]["title"])      #Mostra o título da primeira vaga