import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise SystemExit("Faltou o TELEGRAM_TOKEN no arquivo .env")

#Só esse chat vai ser permitido a falar com o bot
chat_permitido = os.getenv("ALLOWED_CHAT_ID")

if not chat_permitido:
    raise SystemExit("Faltou o ALLOWED_CHAT_ID no arquivo .env")
#Int transforma o texto em número
ALLOWED_CHAT_ID = int(chat_permitido)

#Registra os endereços das requisições com o token junto e mantem os avisos de erros
logging.getLogger("httpx").setLevel(logging.WARNING)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Porteiro: vai ignorar quem tentar acessar ou seja só vai aceitar se for o dono do bot
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return

    await update.message.reply_text("Olá! Eu sou o seu bot de vagas.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__== "__main__":
    main()