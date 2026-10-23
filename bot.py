import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise SystemExit("Faltou o TELEGRAM_TOKEN no arquivo .env")

#Registra os endereços das requisições com o token junto e matem os avisos de erros
logging.getLogger("httpx").setLevel(logging.WARNING)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Só vai me responder quando alguém iniciar o chat com /start

 await update.message.reply_text("Olá! Eu sou o seu bot de vagas.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__== "__main__":
    main()