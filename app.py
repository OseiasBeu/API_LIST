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
def exibir_produtos():
    saida = []

    for data in collection.find():
        saida.append({'cod':data['cod'],'nome_mercado' : data['nome_mercado'], 'nome_produto': data['nome_produto'], 'preco': data['preco']})
    return jsonify({'Resultado':saida})

@app.route('/pesquisar_produto/<nome_produto>', methods=['GET'])
def exibir_produto(nome_produto):
    saida = []

    for data in collection.find({'nome_produto': nome_produto}):
        if data:
            saida.append({'cod': data['cod'],'nome_mercado' : data['nome_mercado'] ,'nome_produto' : data['nome_produto'], 'preco': data['preco']})

    return jsonify({'Resultado': saida})

@app.route('/exibir_produtos_do_mercado/<nome_mercado>', methods=['GET'])
def mostra_produtos(nome_mercado):
    saida = []
    for data in collection.find({'nome_mercado':nome_mercado}):
        if data:
            saida.append({'cod': data['cod'],'nome_mercado' : data['nome_mercado'] ,'nome_produto' : data['nome_produto'], 'preco': data['preco']})

    return jsonify({'Resultado': saida})

#METODOS POST
@app.route('/inserir_produto', methods=['POST'])
def insere_produto():

    print("SAINDO")
    print(request.json)


    nomeMercado = request.json['nome_mercado']
    cod = request.json['cod']
    nome_produto = request.json['nome_produto']
    preco = request.json['preco']

    print("SAINDO")
    print(request.json)
    produto_id = collection.insert({'nome_mercado':nomeMercado,'cod': cod, 'nome_produto': nome_produto, 'preco': preco})
    novo_produto = collection.find_one({'_id': produto_id})

    saida = {'nome_mercado': novo_produto['nome_mercado'],'cod': novo_produto['cod'],'nome_produto': novo_produto['nome_produto'], 'preco': novo_produto['preco']}
    return jsonify(saida)

@app.route('/inserir_produtos', methods=['POST'])
def insere_produtos():

    saida = []
    for data in request.json:
        print(data)
        nomeMercado = data['nome_mercado']
        cod = data['cod']
        nome_produto = data['nome_produto']
        preco = data['preco']
        produto_id = collection.insert({'nome_mercado':nomeMercado,'cod': cod, 'nome_produto': nome_produto, 'preco': preco})
        novo_produto = collection.find_one({'_id': produto_id})
        saida.append({'nome_mercado': novo_produto['nome_mercado'],'cod': novo_produto['cod'],'nome_produto': novo_produto['nome_produto'], 'preco': novo_produto['preco']})

    return jsonify(saida)


#METODOS UPDATE
@app.route('/inclui_campo', methods=['POST'])
def inclui_campo():

    data = request.json
    nome_produto = data['nome_produto']
    status = data['status']


    query = {'nome_produto': nome_produto}
    mod = {"$set":{ 'status': data['status']}}
    options = {"multi": "true"}
#    queries = {query, mod}
    db.collection.update(query, mod, options)
    return "Campo incluido com sucesso!"



#METODOS DELETE
@app.route('/apagar_documentos', methods=['DELETE'])
def apaga_documentos():

    collection.remove({})
    return "Documentos removidos com sucesso!"

#return jsonify('200')

@app.route('/deletar_produtos', methods=['DELETE'])
def deleta_produtos():
    print(request.json)
    data = request.json
    query = {"$and":[{'nome_mercado':data['nome_mercado'] },{'nome_produto':data['nome_produto']}]} 

    collection.remove(query)
    return "Item removido com sucesso!"


