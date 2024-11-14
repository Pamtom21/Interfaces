from flask import Flask, request
import sqlite3
from PIL import Image
import io

app = Flask(__name__) 

def SaveToBD(nombre, original, R, G, B, Gris):
    connection = sqlite3.connect("database/Imagenes.db") # intenta conectarse a la bd
    cursor = connection.cursor() # crea un cursor para interactuar con la bd
    #ingresa los datos a la bd
    cursor.execute("""
        INSERT INTO T_Img(nombre, original, R, G, B, Gris) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, original, R, G, B, Gris))

    connection.commit()#guarda los cambios en la bd
    connection.close() #cierra la conexion de la bd

#define la ruta en la aplicación web que responde a las solicitudes POST en la url
@app.route('/upload', methods=['POST']) 
def ChangeImage():
    if 'image' not in request.files: # verifica si no se encuentra el archivo, responde con un error 400
        return "No file provided", 400

    file = request.files['image'] #si tiene el archivo 'image' lo guarda
    name = file.filename #obtiene el nombre

    filebytes = file.read() # lee el archivo como bytes
    image = Image.open(io.BytesIO(filebytes)) # abre la imagen de los bytes leidos anterior mente

    r, g, b = image.split() #divide la imagen en los componentes rgb
    gris = image.convert("L") #convierte la imagen en escala de colores grises

    def image_to_bytes(img): 
        img_byte_arr = io.BytesIO() #crea un objeto BytesID para almacenar los bytes de la imagen
        img.save(img_byte_arr, format='JPEG') # guarda el objeto en formato jpg
        return img_byte_arr.getvalue() #devuelve los bytes de la imagen
    
    R = image_to_bytes(r)       #convierte el canal rojo de la imagen en bytes           
    G = image_to_bytes(g)       #convierte el canal verde de la imagen en bytes
    B = image_to_bytes(b)       #convierte el canal azul de la imagen en bytes
    Gris = image_to_bytes(gris)#convierte imagen en escala grises en bytes

    SaveToBD(name, filebytes, R, G, B, Gris) # los guarda en la bd
    return "Imagen almacenada exitosamente", 200 # manejo de errores

if __name__ == '__main__': #Verifica si el archivo se está ejecutando directamente
    app.run(debug=True) #Inicia el servidor web Flask en modo de depuración.