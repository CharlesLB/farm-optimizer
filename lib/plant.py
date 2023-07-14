class Plant:
    def __init__(
        self,
        nome,
        producao_da_casa: float,
        valor: float,
        estacao_da_colheita: list[int],
        tempo_de_frutificacao: int,
        tempo_de_colheita: float,
        tempo_de_plantio: float,
        tempo_de_venda: float,
        custo_de_muda: float,
        producao_por_muda: float,
        remessa: float,
        max: float,
    ):
        self.nome = nome
        self.producao_da_casa = producao_da_casa  # float(int/mês)
        self.valor = valor  # float(R$)
        self.estacao_da_colheita = estacao_da_colheita  # bool[12]
        self.tempo_de_frutificacao = tempo_de_frutificacao  # int(mes)
        self.tempo_de_colheita = tempo_de_colheita  # float(h)
        self.tempo_de_plantio = tempo_de_plantio  # float(h)
        self.tempo_de_venda = tempo_de_venda  # float(h)
        self.custo_de_muda = custo_de_muda  # float(R$)
        self.producao_por_muda = producao_por_muda  # float
        self.remessa = remessa  # int(kg)
        self.max = max  # float(kg)
