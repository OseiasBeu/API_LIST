# Instruções

## Primeiro:
 - Inicie a virtualenv.
> source crudVM/bin/activate

## Segundo:
 - Declare as variáveis de ambiente.
> export FLASK_APP=app.py

> export FLASK_ENV=development

## Terceiro:
 - Inicie o banco de dados mongo.
 - Crie um banco com o nome listas_db
> service mongod start

> use listas_db
 
## Quarto: 
 - Inicie o servidor flask
 > flask run
 
 ## Quinto:
 ### Rotas:
 --------------------------------------------------------------------------------------------------------------------------
 ### GET
 --------------------------------------------------------------------------------------------------------------------------
 - http://localhost:5000/exibir_produtos 
 - http://localhost:5000/pesquisar_produto/mesa
 --------------------------------------------------------------------------------------------------------------------------
 ### POST
 --------------------------------------------------------------------------------------------------------------------------
 - http://localhost:5000/exibir_produtos_do_mercado  (ainda não está funcionando)
 - OBS.:  Está rota serve para pesquisar todos os produtos de um único mercado
 
 ## EM CONSTRUÇÃO
 
```
{
    "nome_mercado":"NOME_DO_MERCADO"
}
```

--------------------------------------------------------------------------------------------------------------------------

- http://localhost:5000/inserir_produto
- OBS.: Essa rota permite incluir um único produto
```
{
	"nome_mercado":"NOME_DO_MERCADO",
	"cod":"CÓDIGO_DO_PRODUTO",
	"nome_produto":"NOME_DO_PRODUTO",
	"preco":"VALOR_DO_PRODUTO"
}

```
  
 --------------------------------------------------------------------------------------------------------------------------
- http://localhost:5000/inserir_produtos
- OBS.: Essa rota serve para inserir mais de um produto

```
[
	{
	"nome_mercado":"NOME_DO_MERCADO",
	"cod":"CÓDIGO_DO_PRODUTO",
	"nome_produto":"NOME_DO_PRODUTO",
	"preco":"VALOR_DO_PRODUTO"
  },
  {
	"nome_mercado":"NOME_DO_MERCADO",
	"cod":"CÓDIGO_DO_PRODUTO",
	"nome_produto":"NOME_DO_PRODUTO",
	"preco":"VALOR_DO_PRODUTO"
  },
  {
	"nome_mercado":"NOME_DO_MERCADO",
	"cod":"CÓDIGO_DO_PRODUTO",
	"nome_produto":"NOME_DO_PRODUTO",
	"preco":"VALOR_DO_PRODUTO"
  },
  {
	"nome_mercado":"NOME_DO_MERCADO",
	"cod":"CÓDIGO_DO_PRODUTO",
	"nome_produto":"NOME_DO_PRODUTO",
	"preco":"VALOR_DO_PRODUTO"
  }
]
```

--------------------------------------------------------------------------------------------------------------------------
### DELETE
--------------------------------------------------------------------------------------------------------------------------

- http://localhost:5000/apagar_documentos
- OBS.: Está rota serve para apagar todos os documentos dento da collection produtos

--------------------------------------------------------------------------------------------------------------------------

- http://localhost:5000/deletar_produtos
- OBS.: Está rota serve para apagar todos os documentos com o produto passado

```
{
  "nome_mercado": "NOME_DO_MERCADO",
  "nome_produto": "NOME_DO_PRODUTO_A_SER_APAGADO"
}

```
--------------------------------------------------------------------------------------------------------------------------
### UPDATE
--------------------------------------------------------------------------------------------------------------------------

## EM CONSTRUÇÃO
