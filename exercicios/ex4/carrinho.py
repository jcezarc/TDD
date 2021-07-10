from collections import Counter
from exercicios.ex4.produto import Produto

FORMAT_FLOAT = lambda v: '{:.2f}'.format(v).rjust(10)

class Carrinho:
    def __init__(self):
        self.rascunho = Counter()
        self.lista_produtos = []
        self.log = ''

    def incrementa_produto(self, produto, quantidade=1):
        if isinstance(produto, str):
            nome_produto = produto
        else:
            nome_produto = produto.nome
        quantidade = self.rascunho[nome_produto] + quantidade
        if quantidade < 1:
            self.rascunho.pop(nome_produto, None)
        else:
            self.rascunho[nome_produto] = quantidade
        self.lista_produtos = []

    def extrai_produto(self, nome_produto):
        self.lista_produtos = []
        return self.rascunho.pop(nome_produto)

    def unidades(self):
        """
        Quantos tipos de produtos
        diferentes tem no carrinho
        """
        return len(self.rascunho)

    def obtem_lista_produtos(self):
        if self.lista_produtos:
            return
        lista = []
        for item, quantidade in self.rascunho.items():
            produto = Produto.localiza(item)
            if not produto:
                print('Produto {} não encontrado no estoque'.format(item))
                continue
            lista.append((produto,quantidade))
        self.lista_produtos = lista

    def valor_total(self):
        self.obtem_lista_produtos()
        total = 0
        self.log = ''
        for produto, quantidade in self.lista_produtos:
            self.log += '\n\t{}: {} x {} = {}'.format(
                produto.nome[:30].ljust(30),
                FORMAT_FLOAT(produto.valor),
                str(quantidade).rjust(5),
                FORMAT_FLOAT(produto.valor * quantidade)
            )
            total += produto.valor * quantidade
        return total

    def volume_para_transportar(self):
        self.obtem_lista_produtos()
        carga = 0
        for produto, quantidade in self.lista_produtos:
            carga += produto.dimensoes * quantidade
        return carga
