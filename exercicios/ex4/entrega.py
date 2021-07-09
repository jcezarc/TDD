class ServicoEntregas:
    def valor_frete(self, usuario):
        carrinho = usuario.carrinho
        if not carrinho:
            return 0.00
        volume = carrinho.volume_para_transportar()
        return volume * self.custo_por_regiao(usuario.CEP)

    def custo_por_regiao(self, CEP):
        raise Exception('''
        Método "custo_por_regiao" não implementado em ServicoEntregas
         Use uma classe especializada para chamar esse método.
        ''')


class Correios(ServicoEntregas):
    def custo_por_regiao(self, CEP):
        cidade, zona, distrito = (
            int(CEP[:2]),
            int(CEP[2:5]),
            int(CEP[5:]),
        )
        SP_Capital = cidade in range(9)
        SP_Interior = cidade in range(12, 19)
        SP_Litoral = cidade == 11
        if SP_Capital:
            taxa = 4
            if zona < 5:
                taxa -= 0.5
            if distrito > 100:
                taxa += 1
        elif SP_Interior:
            taxa = 5
        elif SP_Litoral:
            taxa = 6
        return taxa


class API_Externa(ServicoEntregas):
    '''
    Simula uma API externa
    '''

    def origem(self):
        # --- Como se fosse o CEP de onde a mercadoria será enviada (~RJ)
        return '29900000'

    def custo_por_regiao(self, CEP):
        distancia = int(self.origem()) - int(CEP)
        return abs(distancia) / 4000000
