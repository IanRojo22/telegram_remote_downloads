import os

from telegram import Update
from telegram.ext import  CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes

import nest_asyncio
import asyncio

import qbittorrentapi
import myjdapi

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener variables de entorno
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
QB_SERVER = os.getenv('QB_SERVER')
QB_USERNAME = os.getenv('QB_USERNAME')
QB_PASSWORD = os.getenv('QB_PASSWORD')
JD_USERNAME = os.getenv('JD_USERNAME')
JD_PASSWORD = os.getenv('JD_PASSWORD')  
JD_DEVICE_NAME = os.getenv('JD_DEVICE_NAME')

# Conexión a MyJDownloader
try:
    jd = myjdapi.Myjdapi()
    jd.set_app_key("MyApp")
    jd.connect(JD_USERNAME, JD_PASSWORD)
    jd.update_devices()
    jd_device = jd.get_device(JD_DEVICE_NAME)
except myjdapi.MyjdapiException as e:
    print(f"Error al conectar a MyJDownloader: {str(e)}")

# Conexión a qBittorrent
try:
    qb = qbittorrentapi.Client(host=QB_SERVER, username=QB_USERNAME, password=QB_PASSWORD)
except qbittorrentapi.LoginFailed as e:
    print(f"Error de autenticación en qBittorrent: {str(e)}")
except qbittorrentapi.APIConnectionError as e:
    print(f"Error de conexión a qBittorrent: {str(e)}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Envíame un enlace de torrent/magnet o link (Enlaces aceptados: Mega, Mediafire, Youtube) para empezar a descargar.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text.startswith('magnet:') or text.endswith('.torrent'): # Comprueba si el enlace es torrent/magnet
        try:
            qb.torrents_add(urls=text)
            await update.message.reply_text('Torrent agregado exitosamente a qBittorrent.') # En caso que si, lo agrega a qbittorrent
        except qbittorrentapi.APIError as e:
            await update.message.reply_text(f'Error al agregar el torrent: {str(e)}')
        except Exception as e:
            await update.message.reply_text(f'Error desconocido: {str(e)}')
    elif 'youtube.com' in text or 'mediafire.com' in text or 'mega.nz' in text: # En caso que no verifica si el enlace es de mega, mediafire, youtube
        try:
            # Intenta agregar el enlace a JDownloader
            jd_device.linkgrabber.add_links([{"autostart": True, "links": text}])
            await update.message.reply_text('Enlace agregado exitosamente a JDownloader.') 
        except myjdapi.MyjdapiException as e:
            await update.message.reply_text(f'Error al agregar el enlace a JDownloader: {str(e)}')
        except Exception as e:
            await update.message.reply_text(f'Error desconocido: {str(e)}')
    else:
        await update.message.reply_text('Por favor envíame un enlace/link de descarga válido.') # En caso que el mensaje no sea un link/En caso que el enlace no sea valido

def main() -> None:
    try:
        # Crea la aplicación
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        # Añade los Filtros
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Inicia el bot
        application.run_polling()
    except Exception as e:
        print(f"Error al iniciar el bot: {str(e)}")

if __name__ == '__main__':
    nest_asyncio.apply()
    main()