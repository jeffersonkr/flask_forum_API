#!/usr/bin/python3
# -*- coding: utf8 -*-

from server import app
from flask import jsonify, request
from Models import foruns, resposta, usuarios, post

#Criar forum
@app.route("/forum", methods=["POST"])
def criarForum():
    forum = request.get_json()

    foruns.Forum.append(forum)

    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Forum foi criado com sucesso!"
    resposta.Resposta["Dados"] = forum

    return jsonify(resposta.Resposta)

#listar foruns disponiveis
@app.route("/forum", methods=["GET"])
def forunsDisponiveis():
    disponiveis = []
    for i in foruns.Forum:
        if i["Ativo"] == True:
            disponiveis.append(i) 
        else:continue

    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Forum disponiveis foram listados com sucesso!"
    resposta.Resposta["Dados"] = disponiveis

    return jsonify(resposta.Resposta)

#Consulta forum
@app.route("/forum/<id>", methods=["GET"])
def consultaForum(id):
    for i in foruns.Forum:
        if i["Id"] == id:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Forum foi listado com sucesso!"
            resposta.Resposta["Dados"] = i
            break
        else:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Não foi encontrado nenhum forum com essa ID!"
            resposta.Resposta["Dados"] = ""
    
    return jsonify(resposta.Resposta)

#Inativar forum    
@app.route("/forum/inactivate", methods=["POST"])
def inativarForum():
    dados = request.get_json()
    for i in foruns.Forum:
        if i["Id"] == dados["Id"] and i["Id_criador"] == dados["Id_criador"]:
            i["Ativo"] = False
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Forum desativado com sucesso!"
            resposta.Resposta["Dados"] = i
            break

        elif i["Id"] == dados["Id"] and i["Id_criador"] != dados["Id_criador"]:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Id do criador está incorreto."
            resposta.Resposta["Dados"] = i

        else:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Não foi encontrado id desse forum"
            resposta.Resposta["Dados"] = ""

    return jsonify(resposta.Resposta)


#Ativar forum
@app.route("/forum/activate", methods=["POST"])
def ativarForum():
    dados = request.get_json()
    for i in foruns.Forum:
        if i["Id"] == dados["Id"] and i["Id_criador"] == dados["Id_criador"]:
            i["Ativo"] = True
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Forum ativado com sucesso!"
            resposta.Resposta["Dados"] = i

        elif i["Id"] == dados["Id"] and i["Id_criador"] != dados["Id_criador"]:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Id do criador está incorreto."
            resposta.Resposta["Dados"] = i

        else:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Não foi encontrado id desse forum"
            resposta.Resposta["Dados"] = ""

    return jsonify(resposta.Resposta)   

#Inscrever no forum
@app.route("/forum/register", methods=["POST"])
def registerForum():
    inscricao = request.get_json()
    for i in usuarios.Usuario:
        if i["Id"] == inscricao["id_usuario"]:
            usuario = True
            break
        else:
            usuario = False
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Usuario não encontrado!"
            resposta.Resposta["Dados"] = ""

    if usuario == True:
        for k in foruns.Forum:
            if k["Id"] == inscricao["id_forum"] and inscricao["id_usuario"] not in k["Inscritos"]:
                k["Inscritos"].append(i["Id"])

                resposta.Resposta["Status"] = "Sucesso"
                resposta.Resposta["Mensagem"] = "Inscrito com sucesso!"
                resposta.Resposta["Dados"] = k
                break
            elif k["Id"] == inscricao["id_forum"] and inscricao["id_usuario"] in k["Inscritos"]:
                resposta.Resposta["Status"] = "Sucesso"
                resposta.Resposta["Mensagem"] = "Usuario já é inscrito!"
                resposta.Resposta["Dados"] = k
                break
            else:
                resposta.Resposta["Status"] = "Sucesso"
                resposta.Resposta["Mensagem"] = "forum não encontrado!"
                resposta.Resposta["Dados"] = ""
        
        
    return jsonify(resposta.Resposta)

#Remover inscrição do forum
@app.route("/forum/unregister", methods=["POST"])
def unregisterForum():
    unregister = request.get_json()
    for i in usuarios.Usuario:
        if i["Id"] == unregister["id_usuario"]:
            usuario = True
            break
        else:
            usuario = False
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Usuario não encontrado!"
            resposta.Resposta["Dados"] = ""

    if usuario == True:
        for k in foruns.Forum:
            if k["Id"] == unregister["id_forum"] :
                k["Inscritos"].remove(i["Id"])

                resposta.Resposta["Status"] = "Sucesso"
                resposta.Resposta["Mensagem"] = "Removeu a inscricao com sucesso!"
                resposta.Resposta["Dados"] = k
                break
            else:
                resposta.Resposta["Status"] = "Sucesso"
                resposta.Resposta["Mensagem"] = "forum não encontrado!"
                resposta.Resposta["Dados"] = ""
    
        
    return jsonify(resposta.Resposta)



#Criar usuario
@app.route("/usuario", methods=["POST"])
def criarUsuario():
    usuario = request.get_json()
    dados = {"Id": usuario["Id"], "Nome": usuario["Nome"]}

    usuarios.Usuario.append(dados)

    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Usuario foi criado com sucesso!"
    resposta.Resposta["Dados"] = dados

    return jsonify(resposta.Resposta)

#Listar usuario
@app.route("/usuario", methods=["GET"])
def listarUsuario():
    dados = usuarios.Usuario

    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Usuarios listados com sucesso!"
    resposta.Resposta["Dados"] = dados

    return jsonify(resposta.Resposta)



#Criar post
@app.route("/forum/post", methods=["POST"])
def criarPost():
    postagem = request.get_json()
    for i in foruns.Forum:
        if i["Id"] == postagem["Id_forum"] and postagem["Id_criador"] in i["Inscritos"]:
            post.Post.append(postagem)
            i["Post"].append(postagem["Id"])
            i["Data_post"] = postagem["Data_post"]
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Post foi criado com sucesso!"
            resposta.Resposta["Dados"] = post.Post
            break
        else:
            resposta.Resposta["Status"] = "Sucesso"
            resposta.Resposta["Mensagem"] = "Id do forum nao encontrado!"
            resposta.Resposta["Dados"] = ""
    

    return jsonify(resposta.Resposta)

#listar posts dos foruns
@app.route("/forum/<id>/post", methods=["GET"])
def listarPost(id):
    posts = []
    for i in foruns.Forum:
        if id in i["Inscritos"]:
            posts.append(i["Post"])


    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Post listado com sucesso!"
    resposta.Resposta["Dados"] = posts

    return jsonify(resposta.Resposta)

#leitura post(id)
@app.route("/forum/post/<id>", methods=["GET"])
def abrirPost(id):
    mensagens = []
    for i in post.Post:
        for k in foruns.Forum:
            if i["Id_forum"] == k["Id"]:
                if id in k["Inscritos"]:
                    if i["Visivel"] == True:
                        mensagens.append(i["Mensagem"])

    resposta.Resposta["Status"] = "Sucesso"
    resposta.Resposta["Mensagem"] = "Mensagens abertas"
    resposta.Resposta["Dados"] = mensagens

    return jsonify(resposta.Resposta)
