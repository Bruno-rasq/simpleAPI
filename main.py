from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

PRODUTOS = [
  {
    "id": 1,
    "nome": "SmartPhone",
    "preco": 2000.0,
    "descricao": "celuler",
    "disponivel": True
  },

  {
    "id": 2,
    "nome": "computador",
    "preco": 3500.00,
    "descricao": "um computador portatil",
    "disponivel": False
  },
]



class Produto(BaseModel):
  """classe de produto"""

  nome: str
  preco: float
  descricao: Optional[str] = None
  disponivel: Optional[bool] = True




@app.get('/produtos', tags=["produtos"])
def listar_produtos() -> list:
  """lista de produtos."""
  return PRODUTOS


@app.get('/produtos/disponiveis', tags=["produtos"])
def pegar_produtos_disponiveis():
  """buscar produtos disponiveis."""
  produtos_disponiveis = []
  for produto in PRODUTOS:
    if produto["disponivel"]:
      produtos_disponiveis.append(produto)
  return produtos_disponiveis


@app.get("/produtos/{produto_id}", tags=["produtos"])
def buscar_produto(produto_id: int) -> dict:
  """pegar um produto"""
  for produto in PRODUTOS:
    if produto["id"] == produto_id:
      return produto
  return {}


@app.post('/produtos', tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
  """criar um nove produto."""
  produto = produto.dict()
  produto["id"] = len(PRODUTOS) + 1
  PRODUTOS.append(produto)
  return produto


@app.put('/produtos/{produto_id}', tags=["produtos"])
def atualizar_produto(produto_id: int, produto: Produto) -> dict:
  """atualizar produto"""
  for index, prod in enumerate(PRODUTOS):
    if prod["id"] == produto_id:
      PRODUTOS[index] = produto
      return produto
  return {}


@app.delete('/produtos/{id}', tags=["produtos"])
def deletar_produto(id: int) -> dict:
  """deletando um produto."""
  for index, prod in enumerate(PRODUTOS):
    if prod["id"] == id:
      PRODUTOS.pop(index)
      return {"message": "produto deletado com sucesso."}
  return {}
