import telepot
import time
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("twt_token")

bot = telepot.Bot(TOKEN)

def get_updates():
    try:
        updates = bot.getUpdates()
        time.sleep(5)
        return updates[0]["message"]["from"]["id"]
    except Exception as e:
        print(f"Error al obtener actualizaciones: {e}")



get_updates()



