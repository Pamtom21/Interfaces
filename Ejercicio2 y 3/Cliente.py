import random as ra
import requests
import time as tl
import json  # Para convertir a JSON
import vaciar

url = "http://127.0.0.1:5000/upload_json"

def generate():
    # Genera los datos aleatorios
    dMP_data = {
        'N1': [
            {
                'd01': ra.randint(1, 10),
                'd25': ra.randint(1, 10),
                'd10': ra.randint(1, 10)
            }
        ],
        'N2': [
            {
                'd01': ra.randint(1, 10),
                'd25': ra.randint(1, 10),
                'd10': ra.randint(1, 10)
            }
        ],
        'N3': [
            {
                'd01': ra.randint(1, 10),
                'd25': ra.randint(1, 10),
                'd10': ra.randint(1, 10)
            }
        ]
    }
    return dMP_data

if __name__ == '__main__':
    vaciar.vacio
    for k in range(100):
        data = generate()  # Genera los datos aleatorios
        data_json = json.dumps(data)  # Convierte los datos a formato JSON

        
        
        # Enviar la solicitud POST con los datos JSON y la cabecera adecuada
        response = requests.post(url, data=data_json, headers={'Content-Type': 'application/json'})
        tl.sleep(1)
        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            print(f"Solicitud {k+1} enviada correctamente.")
        else:
            print(f"Error en la solicitud {k+1}: {response.status_code}")