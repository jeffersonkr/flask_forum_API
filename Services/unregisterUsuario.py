import requests

url = "http://localhost/forum/unregister"
unregister = {"id_usuario": "2018463", "id_forum": "1856209"}

Retorno = requests.api.post(url, json=unregister).json()
print(Retorno)