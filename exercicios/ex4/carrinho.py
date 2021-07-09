from collections import Counter
from exercicios.ex4.produto import Produto

FORMAT_FLOAT = lambda v: '{:.2f}'.format(v).rjust(10)

class Carrinho:
    def __init__(self):
        self.rascunho = Counter()
        self.lista_produtos = []
        self.log = ''

    def inclui_produto(self, produto, quantidade=1):
        self.lista_produtos = []
        self.rascunho[produto.nome] += quantidade

    def reduz_quantidade(self, nome_produto, quantidade=1):
        quantidade = self.rascunho[nome_produto] - quantidade
        if quantidade < 1:
            self.rascunho.pop(nome_produto)
        else:
            self.rascunho[nome_produto] = quantidade
        self.lista_produtos = []

    def retira_produto(self, nome_produto):
        """
        Não confundir com `reduz_quantidade`:
         Aqui, todos os itens desse tipo de
        produto saõ removidos do carrinho!!
        """
        self.lista_produtos = []
        return self.rascunho.pop(nome_produto)

    def unidades(self):
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
