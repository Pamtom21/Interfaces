import requests
import matplotlib.pyplot as plt
import SendGrapichs

url = "http://127.0.0.1:5000/get_json"
response = requests.post(url) 

d01 = []
d10 = []
d25 = []
data = response.json()        # Datos de la respuesta en formato JSON

for k in range(len(data)):
    d01.append(data[k]["N2"][0]["d01"]) #Se añaden los datos extraidos del nodo 2 cada uno en su lista especifica
    d10.append(data[k]["N2"][0]["d10"])
    d25.append(data[k]["N2"][0]["d25"]) 

tamano = len(d10) # se saca el tamano de una unica lista, ya que estas son iguales en tamano

plt.plot(d01,color = 'red', label = 'd01', zorder = 1)#grafica lineas 
plt.scatter(range(tamano),d01, color = 'red', zorder = 2) #grafica puntos


plt.plot(d10,color = 'green', label = 'd10', zorder = 1)
plt.scatter(range(tamano),d10, color = 'green', zorder = 2)

plt.plot(d25,color = 'blue', label = 'd25', zorder = 1)
plt.scatter(range(tamano),d25, color = 'blue', zorder = 2)
plt.legend()# hace que aparezcan los labels de leyenda
plt.grid(color = 'gray', linestyle = 'dotted') #Muestra los grilleds

plt.xlabel("Cantidad de Datos") #Setea el nombre del label x
plt.ylabel("mg/m3")#Setea el nombre del label y
plt.suptitle("Material Particulado en el Aire", fontsize=12) # Se le asigna el nombre al grafico
plt.savefig('grafico.png') #se guarda el grafico como imagen

SendGrapichs.enviar() # se llama a la funcion de enviar, para compartir el grafico con la ultima persona con la que el bot interactuo
plt.show()# muestra el grafico