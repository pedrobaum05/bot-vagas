import os

from dotenv import load_dotenv

# Lê o arquivo .env e adiciona os dados nas variáveis de ambiente
load_dotenv()

#Puxa o token, caso não ter retorna None
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Caso não ache o TOKEN retorna a mensagem que faltou o TELEGRAM_TOKEN no arquivo .evn
if not TOKEN:
    raise SystemExit("Faltou o TELEGRAM_TOKEN  no arquivo .env")

print("Token carregado com sucesso!")