from exercicios.ex4.carrinho import Carrinho
from exercicios.ex4.entrega import Correios, API_Externa

class Usuario:
    def __init__(self, nome, CEP):
        self.nome = nome
        self.CEP = CEP
        self.carrinho = None

    def faz_compra(self, produtos_para_comprar):
        '''
        Coloca os produtos no carrinho
        :produtos_para_comprar -- É a lista de compras
        '''
        if not self.carrinho:
            self.carrinho = Carrinho()
        for quantidade, produto in produtos_para_comprar:
            self.carrinho.inclui_produto(produto, quantidade)

    def valor_pedido(self, exibe_debug=False):
        total = self.carrinho.valor_total()
        if total < 100:
            entrega = API_Externa()
        else:
            entrega = Correios()
        frete = entrega.valor_frete(self)
        if exibe_debug:
            format_float = lambda v: '{:.2f}'.format(v).rjust(10)
            print('{}: {} + Frete {}: {} = {}'.format(
                self.nome[:13],
                format_float(total),
                entrega.__class__.__name__.ljust(12),
                format_float(frete),
                format_float(total + frete),
            ))
        return total + frete
