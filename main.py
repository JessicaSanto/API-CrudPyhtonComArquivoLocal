# API -> É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de carros
# 2. URL base - localhost
# 3. Endpoints - 
    # localhost/carros(GET)
    # localhost/carros(PUT)
    # localhost/carros(DELETE)
    # localhost/carros id (GET)


# PIP -> é um gerenciador de pacotes para projetos Python. É com ele que instalamos, removemos e atualizamos pacotes em nossos projetos. É similar ao npm e composer. Possui uma página onde nós conseguimos buscar os pacotes disponíveis para utilização.
# https://pypi.org/
# O Flask é um pacote de ferramentas para facilitar o desenvolvimento da nossa API 

from flask import Flask, request, make_response, jsonify
# ******** MÉTODO 1 -> CASO OCORRA O ERRO DA RESPOSTA INVÁLIDA*******
# CASO TENHA DADO ERRO AO RODAR A URL NO INSMONIA, ADICIONAR NO IMPORT ACIMA -> from flask import Flask, make_response, jsonify
# Caso ele apareça que o "response não é valido", o make_responde vai tornar a resposta válida
# Já o jsonify, vai modular a resposta no padrão JSON. SEGUE PARA LINHA DO @APP.ROUTE

# ******** MÉTODO 2 -> CASO OCORRA O ERRO DA RESPOSTA INVÁLIDA*******
# Adicionar no import do Flask -> request 

from bd import Carros
# Esse é o modulo do Flask que vai subir a nossa API localmente
# Abaixo, vamos instaciar o modulo Flask na nossa variavel app 
app = Flask('carros')


# ***********CASO O JSON ESTEJA RETORNANDO OS VALORES EM ORDEM ALFABÉTICA************
app.config['JSON_SORT_KEYS'] = False

# Comando para executar esse servidor -> app.run()
# Teste para verificar que está funcionando
# Entre a instancia do app e o app.run, vamos colocar nossas funções

# A principio, nós não vamos linkar nossa API com um banco de dados. Então vamos criar o arquivo bd.py que fará o papel de simular nosso banco de dados


# *********************************************************************************************************************************************


# **************** PRIMEIRO MÉTODO - VISUALIZAR OS DADOS (GET) ******************
# Criação do primeiro métoodo. Criamos primeiro o def e depois o @app
# def get_carros -> Criamos uma função para retornar a lista de carros 
# @app.route -> precisamos definir que essa função é uma rota para que o flask entenda que aquilo é um metodo que deve ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

# ******** CASO OCORRA O ERRO DA RESPOSTA INVÁLIDA OU PARA DEIXAR UMA MENSAGEM DE RETORNO MAIS BONITA*******
# return make_response(
# jsonify(
#   mensagem='Lista de Carros',
#   dados=Carros
# )
# )


# *********************************************************************************************************************************************


# **************** PRIMEIRO MÉTODO PARTE 2 - VISUALIZAR OS DADOS POR ID (GET) ******************
# Vamos pedir para ele rodar um laço de repetição para que ele procure dentro da lista de Carros, o carro cujo id é igual ao solicitado.
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)
        

# *********************************************************************************************************************************************


# **************** SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST) ******************
# Vamos capturar os dados que estão sendo passados na requisição e armazenar no nosso "banco de dados"
# Adicionar no import do Flask -> request 
# Criação do segundo métoodo. Criamos primeiro o def e depois o @app
# O resquest vai permitir que sejam feitas requisições
# Carros.append(carro) -> Vai adicionar esse carro cadastrado ao nosso banco de dados 

@app.route('/carros', methods=['POST'])
def create_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso',
            carro=carro
        ))

# ******** PARA DEIXAR UMA MENSAGEM DE RETORNO MAIS BONITA -> JSONIFY*******


# *********************************************************************************************************************************************
# **************** TERCEIRO MÉTODO - EDITAR DADOS (PUT) ******************


@app.route('/carros/<int:id>',methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice,carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
        

# *********************************************************************************************************************************************
# **************** TERCEIRO MÉTODO - EDITAR DADOS (PUT) ******************


@app.route('/carros/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice,carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem": "Carro excluído com sucesso"})
        

# Vamos para o INSOMINIA e executa a GET com a URL do terminal 
# Em seguida vai no método POST e cria os seguintes valores:
# {
	# "id": 6,
	# "marca": "FIAT",
	# "modelo": "Elba",
	# "ano": 1997
# } 
# Depois executa o Get novamente

# Comando para executar esse servidor
app.run(port=5000, host='localhost', debug=True)
# Teste para verificar que está funcionando