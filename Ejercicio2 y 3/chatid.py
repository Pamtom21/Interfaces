import telepot
import time
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("twt_token")# el token esta en variables de entorno

bot = telepot.Bot(TOKEN) #se inicializa el bot mediante el token, ya que este es necesario para controlarlo

def get_updates():
    try:
        updates = bot.getUpdates()#entrega un array con las personas que han interactuado con el bot
        id= updates[len(updates)-1]["message"]["from"]["id"]
        nombre = updates[len(updates)-1]["message"]["from"]["first_name"] + " " +updates[len(updates)-1]["message"]["from"]["last_name"]
        return id, nombre  #esto devuelve el id y nombre del chat del ultimo en interactuar
    except Exception as e:
        print(f"Error al obtener actualizaciones: {e}") #manejo de errores



get_updates()



