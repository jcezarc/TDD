from exercicios.ex4.produto import Produto

FORMAT_FLOAT = lambda v: '{:.2f}'.format(v).rjust(10)
IDX_CAMPO_QUANTIDADE = -1

class ErroItemNaoEncontrado(Exception):
    pass

class Carrinho:
    def __init__(self):
        self.itens = {}
        self.log = ''

    def incrementa_item(self, produto, incremento=1):
        if isinstance(produto, str):
            nome_produto = produto
            produto = None
        else:
            nome_produto = produto.nome
        item = self.item_por_nome(nome_produto)
        if not item:
            if not produto:
                raise ErroItemNaoEncontrado()
            quantidade = 0
        else:
            produto, quantidade = item
        quantidade += incremento
        if quantidade < 1:
            self.itens.pop(nome_produto, None)
        else:
            self.itens[nome_produto] = (produto, quantidade)

    def item_por_nome(self, nome_produto):
        return self.itens.get(nome_produto, None)

    def quantidade_produto(self, nome_produto):
        item = self.item_por_nome(nome_produto)
        if not item:
            return 0
        return item[IDX_CAMPO_QUANTIDADE]

    def vazio(self):
        return len(self.itens) == 0

    def valor_total(self):
        total = 0
        self.log = ''
        for produto, quantidade in self.itens.values():
            self.log += '\n\t{}: {} x {} = {}'.format(
                produto.nome[:30].ljust(30),
                FORMAT_FLOAT(produto.valor),
                str(quantidade).rjust(5),
                FORMAT_FLOAT(produto.valor * quantidade)
            )
            total += produto.valor * quantidade
        return total

    def volume_para_transportar(self):
        carga = 0
        for produto, quantidade in self.itens.values():
            carga += produto.dimensoes * quantidade
        return carga
