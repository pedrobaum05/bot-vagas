#Vai buscar/ trazer as vagas com auxílio da API do GitHub

import requests

#Endereço da API que vai direto para o repositório das vagas 
URL = "https://api.github.com/repos/backend-br/vagas/issues"
#Verifica quem está pedindo os dados
HEADERS = {"User-Agent": "bot-vagas-pedro"}

def buscar_vagas():
    params = {"state": "open", "per_page": 3}
    try:
        resposta = requests.get(URL, params=params, headers=HEADERS, timeout=10)
    except requests.exceptions.Timeout:
        print("Demorou demais. Tento de novo mais tarde")
        return [] #Retorna os dados da lista vazia, pois não achou nenhuma vaga
    except requests.exceptions.RequestException:
        print("Erro de conexão ou de requisição.")
        return []

    if resposta.status_code != 200:
        print(f"A API respondeu com erro: {resposta.status_code}")
        return []
    
    return resposta.json()

#Uso das funções
vagas = buscar_vagas()
print("Quantidade de vagas:", len(vagas))
if vagas:
    print(vagas[0]["title"])