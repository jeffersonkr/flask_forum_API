import requests

url = "http://localhost/forum/activate"
forum = {"Id": "1846701", "Id_criador": "2018622"}

Retorno = requests.api.post(url, json=forum).json()
print(Retorno)