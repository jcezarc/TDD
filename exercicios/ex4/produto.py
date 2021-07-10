ERRO_NOME_EM_BRANCO = 1
ERRO_VALOR_INVALIDO = 2
ERRO_PRO_SEM_VOLUME = 3

class Produto:
    catalogo = {}
    erro = 0
    def __new__(cls, nome, valor, dimensoes):
        '''
        Produto
        :dimensoes -- Um fator hipotético para fins de transporte
                    (ver serviço de entregas em `entregas.py`)
        '''
        Produto.erro = Produto.valida(nome, valor, dimensoes)
        if Produto.erro:
            return None
        obj = Produto.localiza(nome)
        if not obj:
            obj = object.__new__(cls)
            Produto.catalogo[nome] = obj
        obj.nome = nome
        obj.valor = valor
        obj.dimensoes = dimensoes
        return obj

    @staticmethod
    def valida(nome, valor, dimensoes):
        if not nome.strip():
            return ERRO_NOME_EM_BRANCO
        if valor <= 0:
            return ERRO_VALOR_INVALIDO
        if dimensoes < 1:
            return ERRO_PRO_SEM_VOLUME
        return 0

    @classmethod
    def localiza(cls, busca):
        return Produto.catalogo.get(busca)
