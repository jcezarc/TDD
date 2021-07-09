from exercicios.ex4.carrinho import Carrinho, FORMAT_FLOAT
from exercicios.ex4.entrega import Correios, API_Externa

class Usuario:
    def __init__(self, nome, CEP):
        self.nome = nome
        self.CEP = CEP
        self.carrinho = None
        self.log = ''

    def faz_compra(self, produtos_para_comprar):
        '''
        Coloca os produtos no carrinho
        :produtos_para_comprar -- É a lista de compras
        '''
        if not self.carrinho:
            self.carrinho = Carrinho()
        for quantidade, produto in produtos_para_comprar:
            self.carrinho.inclui_produto(produto, quantidade)

    def soma_pedido(self):
        total = self.carrinho.valor_total()
        if total < 100:
            entrega = API_Externa()
        else:
            entrega = Correios()
        frete = entrega.valor_frete(self)
        self.log = '{}: {} + Frete {}: {} = {}'.format(
            self.nome[:13],
            FORMAT_FLOAT(total),
            entrega.__class__.__name__.ljust(12),
            FORMAT_FLOAT(frete),
            FORMAT_FLOAT(total + frete),
        )
        return total + frete

    def emite_relatorio(self, detalhado=False):
        self.soma_pedido()
        print('='*50)
        print(self.log)
        if detalhado:
            print(self.carrinho.log)
        print('-'*50)
