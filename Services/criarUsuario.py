import requests
import random, datetime
import sys, os

sys.path.insert(0, ("/".join(os.path.realpath(__file__).split("/")[:-2] + [""])))
from Models import usuarios

def criarId():
    id_ = str(datetime.date.today().year) + str(random.randint(random.randint(000, 999), 999))
    for i in usuarios.Usuario:
        if id_ in i["Id"]:
            criarId()

    return id_

url = "http://localhost/usuario"
usuario = {"Id": criarId(), "Nome": "Felipe"}

Retorno = requests.api.post(url, json=usuario).json()
print(Retorno)