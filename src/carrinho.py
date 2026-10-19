FRETE = 20.00
LIMITE_FRETE_GRATIS = 150.00

class Carrinho:
          def __init__(self):
              self._itens = {}

          def adicionar_item(self, nome, preco, quantidade=1):
              if preco <= 0:
                raise ValueError("Preco deve ser > 0")
              if quantidade <= 0:
                raise ValueError("Quantidade deve ser > 0")
              if nome in self._itens:
                self._itens[nome]["quantidade"] += quantidade
              else:
                self._itens[nome] = {"nome": nome, "preco": preco, "quantidade": quantidade}

          def remover_item(self,nome):
              if nome not in self._itens:
                raise ValueError(f"Item '{nome}' nao esta no carrinho")
              del self._itens[nome]

          def show(self):
              return [dict(item) for item in self._itens.values()]

          def total(self):
              if not self._itens:
                return 0.00
              subtotal = round(sum(i["preco"] * i["quantidade"] for i in self._itens.values()), 2)
              frete = 0.0 if subtotal >= LIMITE_FRETE_GRATIS else FRETE 
              return round(subtotal + frete, 2)