import telepot as tl
import chatid
token = chatid.TOKEN

id = chatid.get_updates()

Bot = tl.Bot(token)
def enviar():
    with open('grafico.png', 'rb') as graf:
        Bot.sendPhoto(id, graf)
