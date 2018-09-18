import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client.listas_db
collection = db.produtos

@app.route('/')
def hello_world():
    return 'Teste Flask'

@app.route('/post/<int:post_id>')
def show_post(post_id):
      # show the post with the given id, the id is an integer
    return 'Teste Post com id %d' % post_id

#METODOS GET
@app.route('/exibir_produtos', methods=['GET'])
def exibir_listas():
    saida = []

    for data in collection.find():
        saida.append({'cod':data['cod'], 'nome': data['nome'], 'preco': data['preco']})
    return jsonify({'Resultado':saida})

@app.route('/pesquisar_produtos/<nome>', methods=['GET'])
def exibir_produto(nome):
    saida = []

    for data in collection.find({'nome': nome}):
        if data:
            saida.append({'cod': data['cod'],'nome_mercado' : data['nome_mercado'] ,'nome' : data['nome'], 'preco': data['preco']})

    return jsonify({'Resultado': saida})


#METODOS POST
@app.route('/inserir_produto', methods=['POST'])
def insere_produto():

    print("SAINDO")
    print(request.json)


    nomeMercado = request.json['nome_mercado']
    cod = request.json['cod']
    nome = request.json['nome']
    preco = request.json['preco']

    print("SAINDO")
    print(request.json)
    produto_id = collection.insert({'nome_mercado':nomeMercado,'cod': cod, 'nome': nome, 'preco': preco})
    novo_produto = collection.find_one({'_id': produto_id})

    saida = {'nome_mercado': novo_produto['nome_mercado'],'cod': novo_produto['cod'],'nome': novo_produto['nome'], 'preco': novo_produto['preco']}
    return jsonify(saida)

@app.route('/inserir_produtos', methods=['POST'])
def insere_produtos():

    saida = []
    for data in request.json:
        print(data)
        nomeMercado = data['nome_mercado']
        cod = data['cod']
        nome = data['nome']
        preco = data['preco']
        produto_id = collection.insert({'nome_mercado':nomeMercado,'cod': cod, 'nome': nome, 'preco': preco})
        novo_produto = collection.find_one({'_id': produto_id})
        saida.append({'nome_mercado': novo_produto['nome_mercado'],'cod': novo_produto['cod'],'nome': novo_produto['nome'], 'preco': novo_produto['preco']})

    return jsonify(saida)

#METODOS DELETE
@app.route('/apagar_documentos', methods=['DELETE'])
def apaga_documentos():

    collection.remove({})
    return "Documentos removidos com sucesso!"

#return jsonify('200')

@app.route('/deletar_produtos', methods=['DELETE'])
def deleta_produtos():
    print(request.json)
    nomeMercado = request.json['nome_mercado']
    nomeItem = request.json['nome']

#    collection.find("nome_mercado"
    collection.remove({nomeMercado : { "$eq": "nomeItem" }})
    return "Item removido com sucesso!"
