import requests


url = url = "http://127.0.0.1:5000/delete_json"
def borrar():
    vacio = requests.post(url)
    response = vacio.json()
    print(response)

