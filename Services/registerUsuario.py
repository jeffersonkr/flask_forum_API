import requests

url = "http://localhost/forum/register"
register = {"id_usuario": "2018927", "id_forum": "1883121"}

Retorno = requests.api.post(url, json=register).json()
print(Retorno)