#Vai buscar/ trazer as vagas com auxílio da API do GitHub

import requests

#Endereço da API que vai direto para o repositório das vagas 
URL = "https://api.github.com/repos/backend-br/vagas/issues"
#Verifica quem está pedindo os dados
HEADERS = {"User-Agent": "bot-vagas-pedro"}

def buscar_vagas(pagina=1): #Valor padrão da busca de vagas 
    params = {"state": "open", "per_page": 3, "page": pagina}
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
vagas_pagina_1 = buscar_vagas(1)
vagas_pagina_2 = buscar_vagas(2)

print("Página 1:", vagas_pagina_1[0]["title"])
print("Página 2:", vagas_pagina_2[0]["title"])