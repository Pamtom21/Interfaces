import telepot as tl
import chatid
token = "7665277392:AAHRRlC_5ZhdaQh-VqtvyazJE7l2Mheaho4"

id = chatid.get_updates()

Bot = tl.Bot(token)
def enviar():
    with open('grafico.png', 'rb') as graf:
        Bot.sendPhoto(id, graf)
