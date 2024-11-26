import requests
import os 
import time

images = "IMG" #ruta de las imagens
url = "http://127.0.0.1:5000/upload" #url del servidor

def send_image(image):
    with open(image, 'rb') as img_file: #recibe la imagen y la lee de forma binaria
        name = os.path.basename(image) #obtiene el nombre usando os.path.basename

        files = {'image': (name, img_file, 'image/jpg')} #contiene la imagen
        data = {'nombre': name} # contiene el nombre de la imagen
        response = requests.post(url, files=files, data=data) #envia una solicitud a la url, con la imagen y los datos
    
        if response.status_code == 200: #manejo de errores
            print(f"Imagen '{name}' enviada exitosamente.")
        else:
            print(f"Error al enviar '{name}': {response.json()}")

if __name__ == '__main__': #inicia un bucle 
    i = 0 #iniciamos en 0
    for image_name in os.listdir(images): #devuelve una lista con los nombres de los archivos del directorio images.
        if i >= 10: #verifica si se pasa de las 10 imagenes
            break# de ser asi se rompe
        image_path = os.path.join(images, image_name) # combina la imagen, con el nombre
        send_image(image_path) # envia la imagen al servidor

        i += 1
        time.sleep(3) # espera 3 segundos antes de enviar la siguiente imagen