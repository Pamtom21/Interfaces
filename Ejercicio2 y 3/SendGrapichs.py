import telepot as tl
import chatid
token = chatid.TOKEN

id, nombre = chatid.get_updates() # esta es la id que se obtiene en el codigo de chatid

Bot = tl.Bot(token) # se inicializa el bot
def enviar():
    with open('grafico.png', 'rb') as graf:# se abre la imagen y se envia
        Bot.sendPhoto(id, graf)
        print(f"Grafico enviado a {nombre}")
