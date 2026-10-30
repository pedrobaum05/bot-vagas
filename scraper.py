#Vai buscar/ trazer as vagas com auxílio da API do GitHub

import requests
import time

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

def buscar_todas_as_vagas(max_paginas=3):
    todas = [] #Vai juntar todas as vagas das paginas

    for pagina in range(1, max_paginas + 1):
        vagas_da_pagina = buscar_vagas(pagina)

        if not vagas_da_pagina:
            break

        todas.extend(vagas_da_pagina) #Junta todas as vagas em uma lista extendida 
        time.sleep(1) #Dá uma pausa 

    return todas

#Uso das funções
vagas = buscar_todas_as_vagas()
print("Total de vagas:", len(vagas))