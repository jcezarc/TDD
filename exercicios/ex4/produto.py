class Produto:
    catalogo = {}
    def __new__(cls, nome, valor, dimensoes):
        '''
        Produto
        :dimensoes -- Um fator hipotético para fins de transporte
                    (ver serviço de entregas em `entregas.py`)
        '''
        obj = Produto.localiza(nome)
        if not obj:
            obj = object.__new__(cls)
            Produto.catalogo[nome] = obj
        obj.config(nome, valor, dimensoes)
        return obj

    def config(self, nome, valor, dimensoes):
        self.nome = nome
        self.valor = valor
        self.dimensoes = dimensoes

    @classmethod
    def localiza(cls, busca):
        return Produto.catalogo.get(busca)
