import string


class Plant:
    def __init__(
        self,
        nome: string,
        produção_da_casa: float,
        valor: float,
        estação_da_colheita: list[12],
        tempo_de_frutificação: int,
        tempo_de_colheita: float,
        tempo_de_plantio: float,
        tempo_de_venda: float,
        custo_de_muda: float,
        produção_por_muda: float,
        remessa: float,
        max: float,
    ):
        self.nome = nome
        self.produção_da_casa = produção_da_casa  # float(int/mês)
        self.valor = valor  # float(R$)
        self.estação_da_colheita = estação_da_colheita  # bool[12]
        self.tempo_de_frutificação = tempo_de_frutificação  # int(mes)
        self.tempo_de_colheita = tempo_de_colheita  # float(h)
        self.tempo_de_plantio = tempo_de_plantio  # float(h)
        self.tempo_de_venda = tempo_de_venda  # float(h)
        self.custo_de_muda = custo_de_muda  # float(R$)
        self.produção_por_muda = produção_por_muda  # float
        self.remessa = remessa  # int(kg)
        self.max = max  # float(kg)
