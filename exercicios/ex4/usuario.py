from carrinho import Carrinho
from entrega import Correios, API_Externa

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

    def valor_pedido(self):
        total = self.carrinho.calcula_total()
        if total < 100:
            entrega = API_Externa()
        else:
            entrega = Correios()
        frete = entrega.valor_frete(self)
        print('\tValor do frete:', frete)
        total += frete
        return total
