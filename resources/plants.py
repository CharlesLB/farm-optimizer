class Plant:
    def __init__(
        self,
        nome,
        producao_da_casa,
        valor,
        estacao_da_colheita,
        tempo_de_frutificação,
        tempo_de_colheita,
        tempo_de_plantio,
        tempo_de_venda,
        custo_de_muda,
        producao_por_muda,
        remessa,
        max,
    ):
        self.nome = nome
        self.producao_da_casa = producao_da_casa  # float(int/mês)
        self.valor = valor  # float(R$)
        self.estacao_da_colheita = estacao_da_colheita  # bool[12]
        self.tempo_de_frutificação = tempo_de_frutificação  # int(mes)
        self.tempo_de_colheita = tempo_de_colheita  # float(h)
        self.tempo_de_plantio = tempo_de_plantio  # float(h)
        self.tempo_de_venda = tempo_de_venda  # float(h)
        self.custo_de_muda = custo_de_muda  # float(R$)
        self.producao_por_muda = producao_por_muda  # float
        self.remessa = remessa  # int(kg)
        self.max = max  # float(kg)
