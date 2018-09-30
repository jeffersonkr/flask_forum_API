from server import app
from Models import resposta
from flask import jsonify

@app.errorhandler(404)
def TratarNaoEncontrado(error):
    resposta.Resposta["Status"] = "Erro"
    resposta.Resposta["Mensagem"] = "Acao nao existente"
    return jsonify(resposta.Resposta)

@app.errorhandler(500)
def TratarNaoEncontrado2(error):
    resposta.Resposta["Status"] = "Erro"
    resposta.Resposta["Mensagem"] = "Um problema critico foi encontrado. Erro{0}".format(error)
    return jsonify(resposta.Resposta)