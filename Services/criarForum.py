import requests
import random, datetime
import sys, os

sys.path.insert(0, ("/".join(os.path.realpath(__file__).split("/")[:-2] + [""])))
from Models import foruns

def criarId():
    id_ = str(datetime.date.today().year)[2:] + str(random.randint(random.randint(00000, 99999), 99999))
    for i in foruns.Forum:
        if id_ in i["Id"]:
            criarId()

    return id_

url = "http://localhost/forum"
postagens = []
id_criador = "2018686"
data_hora = str(datetime.datetime.now()).split(".")[0]
forum = {"Id": criarId(), "Id_criador": id_criador , "data/hora": data_hora, "Titulo": "Nada", "Descricao": "forum sobre nada", "Ativo": True, "Inscritos": [id_criador], "Data_post": "", "Post": postagens}

Retorno = requests.api.post(url, json=forum).json()
print(Retorno)