ERRO_NOME_EM_BRANCO = 1
ERRO_VALOR_INVALIDO = 2
ERRO_PRO_SEM_VOLUME = 3

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
        obj.valida(nome, valor, dimensoes)
        return obj

    def valida(self, nome, valor, dimensoes):
        if not nome.strip():
            self.erro = ERRO_NOME_EM_BRANCO
            return
        self.nome = nome
        if valor <= 0:
            self.erro = ERRO_VALOR_INVALIDO
            return
        self.valor = valor
        if dimensoes < 1:
            self.erro = ERRO_PRO_SEM_VOLUME
            return
        self.dimensoes = dimensoes
        self.erro = 0

    @classmethod
    def localiza(cls, busca):
        return Produto.catalogo.get(busca)
