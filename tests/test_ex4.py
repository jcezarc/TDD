import sys
sys.path.append('.')
sys.path.append('..')
from exercicios.ex4.produto import (
    Produto, ERRO_NOME_EM_BRANCO,
    ERRO_VALOR_INVALIDO, ERRO_PRO_SEM_VOLUME
)
from exercicios.ex4.usuario import (
    Usuario, ErroCEPInvalido
)
from exercicios.ex4.carrinho import (
    Carrinho, ErroItemNaoEncontrado
)

CHOCOLATE_BARRA_LINDT = {
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
            Produto(**CHOCOLATE_BARRA_LINDT)
        ),
    ])
    Sheila = Usuario('Sheila Kely Jota', '09542101')
    Sheila.faz_compra([
        (
            1,
            Produto(**CHOCOLATE_BARRA_LINDT)
        ),
        (
            3,
            Produto('Sorvete Haagen Daz', 16.33, 1.05)
        ),
    ])
    return Elias, Sheila

def test_frete():
    valores_esperados = [(25, 26), (21, 22)]
    for pessoa, faixa in zip(pessoas_mercado(), valores_esperados):
        total, frete = pessoa.fecha_pedido()
        if total < 100:
            assert pessoa.nome_serv_entrega == 'API_Externa'
        else:
            assert pessoa.nome_serv_entrega ==  'Correios'
        min, max = faixa
        assert frete >= min and frete <= max

def test_carrinho_vazio():
    carrinho = Carrinho()
    assert carrinho.vazio()

def test_carrinho_prod_duplicado():
    carrinho = Carrinho()
    qtd_esperada = 3
    produto_teste = Produto(**CHOCOLATE_BARRA_LINDT)
    for _ in range(qtd_esperada):        
        carrinho.incrementa_item(produto_teste)
    quantidade = carrinho.quantidade_produto(CHOCOLATE_BARRA_LINDT['nome'])
    assert quantidade == qtd_esperada

def test_zerar_quantidade():
    carrinho = Carrinho()
    carrinho.incrementa_item(
        Produto(**CHOCOLATE_BARRA_LINDT)
    )
    nome_produto = CHOCOLATE_BARRA_LINDT['nome']
    carrinho.incrementa_item(
        nome_produto,
        -1 # -- valor negativo reduz a quantidade
    )
    item = carrinho.item_por_nome(nome_produto)
    assert not item

def test_falha_alterar_quantidade():
    erro_previsto = False
    carrinho = Carrinho()
    try:
        carrinho.incrementa_item('Xyz')
    except ErroItemNaoEncontrado:
        erro_previsto = True
    assert erro_previsto

def test_volume():
    pessoas = pessoas_mercado()
    volumes_esperados = [6.4, 4.2]
    for pessoa, esperado in zip(pessoas, volumes_esperados):
        volume = pessoa.carrinho.volume_para_transportar()
        assert volume == esperado

def test_reajuste_preco():
    Sheila = pessoas_mercado()[1]
    nome, valor, dimensoes = CHOCOLATE_BARRA_LINDT.values()
    valor = 10.4
    Sheila.faz_compra([
        (1, Produto(nome, valor, dimensoes))
    ])
    total = Sheila.fecha_pedido()[0]
    assert total > 69.78 and total < 69.80

def test_produto_em_branco():
    produto = Produto('', 0, 0)
    assert Produto.erro == ERRO_NOME_EM_BRANCO

def test_produto_valor_invalido():
    produto = Produto('Sem valor', 0, 0)
    assert Produto.erro == ERRO_VALOR_INVALIDO

def test_produto_sem_volume():
    produto = Produto('Peso negativo', 2.5, -3)
    assert Produto.erro == ERRO_PRO_SEM_VOLUME

def test_CEP_invalido():
    erro_previsto = False
    try:
        Usuario(CEP='xxx ', nome='')
    except ErroCEPInvalido:
        erro_previsto = True
    assert erro_previsto


EX4_TEST_CASES = [
    test_frete,
    test_carrinho_vazio,
    test_carrinho_prod_duplicado,
    test_zerar_quantidade,
    test_falha_alterar_quantidade,
    test_volume,
    test_reajuste_preco,
    test_produto_em_branco,
    test_produto_valor_invalido,
    test_produto_sem_volume,
    test_CEP_invalido,
]


if __name__ == '__main__':
    for p in pessoas_mercado():
        p.emite_relatorio(True)
