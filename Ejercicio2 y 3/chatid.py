import telepot
import time
TOKEN = '7665277392:AAHRRlC_5ZhdaQh-VqtvyazJE7l2Mheaho4'

bot = telepot.Bot(TOKEN)


def get_updates():
    try:
        updates = bot.getUpdates()
        time.sleep(5)
        return updates[0]["message"]["from"]["id"]
    except Exception as e:
        print(f"Error al obtener actualizaciones: {e}")



get_updates()



