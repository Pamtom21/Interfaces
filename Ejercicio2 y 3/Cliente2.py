import requests
import matplotlib.pyplot as plt
import SendGrapichs

url = "http://127.0.0.1:5000/get_json"
response = requests.post(url)  # Usar GET en lugar de POST

d01 = []
d10 = []
d25 = []
data = response.json()        # Datos de la respuesta en formato JSON

for k in range(len(data)):
    d01.append(data[k]["N2"][0]["d01"])
    d10.append(data[k]["N2"][0]["d10"])
    d25.append(data[k]["N2"][0]["d25"]) 

tamano = len(d10)

plt.plot(d01,color = 'red', label = 'd01', zorder = 1)
plt.scatter(range(tamano),d01, color = 'red', zorder = 2)


plt.plot(d10,color = 'green', label = 'd10', zorder = 1)
plt.scatter(range(tamano),d10, color = 'green', zorder = 2)

plt.plot(d25,color = 'blue', label = 'd25', zorder = 1)
plt.scatter(range(tamano),d25, color = 'blue', zorder = 2)
plt.legend()
plt.grid(color = 'gray', linestyle = 'dotted')

plt.xlabel("Cantidad de Datos")
plt.ylabel("mg/m3")
plt.suptitle("Material Particulado en el Aire", fontsize=12)
plt.savefig('grafico.png') 

SendGrapichs.enviar()
plt.show()