import requests
import random, datetime
import sys, os

sys.path.insert(0, ("/".join(os.path.realpath(__file__).split("/")[:-2] + [""])))
from Models import post

def criarId():
    id_ = str(datetime.date.today().year)[2:] + str(random.randint(random.randint(000, 999), 999))
    for i in post.Post:
        if id_ in i["Id"]:
            criarId()

    return id_

url = "http://localhost/forum/post"
id_criador = "2018857"
id_forum = "1883121"
data_hora = str(datetime.datetime.now()).split(".")[0]
postagem = {"Id": criarId(), "Id_criador": id_criador, "Id_forum": id_forum, "Data_post": data_hora, "Mensagem": "Olá Mundo!!! WUal!!!! funciona", "Visivel": True}

Retorno = requests.api.post(url, json=postagem).json()
print(Retorno)