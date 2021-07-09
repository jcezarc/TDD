from exercicios.ex4.produto import Produto
from exercicios.ex4.usuario import Usuario

DADOS_CHOCOLATE_LINDT = {
    'nome': 'Chocolate barra 250g Lindit',
    'valor': 11.27,
    'dimensoes': 1.05,
}


def pessoas_mercado():
    Elias = Usuario('Elias Saraiva', '01103020')
    Elias.faz_compra([
        (
            2,
            Produto('Queijo Estepe Tirolez', 28.35, 1.1)
        ),
        (
            4,
            Produto(**DADOS_CHOCOLATE_LINDT)
        ),
    ])
    Sheila = Usuario('Sheila Kely Jota', '09542101')
    Sheila.faz_compra([
        (
            1,
            Produto(**DADOS_CHOCOLATE_LINDT)
        ),
        (
            3,
            Produto('Sorvete Haagen Daz', 16.33, 1.05)
        ),
    ])


if __name__ == '__main__':
    mostra = lambda p: '{}: {:.2f}'.format(
        p.nome,
        p.valor_pedido()
    )
    resumo = [mostra(p) for p in pessoas_mercado()]
    print('\n'.join(resumo))
