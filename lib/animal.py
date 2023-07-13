import string


class Animal:
    def __init__(
        self,
        nome: string,
        produção_da_casa: float,
        valor: float,
        tempo_de_cuidado: float,
        custo_por_animal: float,
        tempo_de_venda: float,
        tempo_de_produção: float,
        remessa: float,
        numero_de_femeas: int,
        numero_de_machos: int,
    ):
        self.nome = nome
        self.produção_da_casa = produção_da_casa  # float(int/mês)
        self.valor = valor  # float(R$)
        self.tempo_de_cuidado = tempo_de_cuidado  # float(horas/dia/animal)
        self.custo_por_animal = custo_por_animal  # float(R$/mês/animal)
        self.tempo_de_venda = tempo_de_venda  # float(h/remessa)
        self.tempo_de_produção = tempo_de_produção  # float(int/dias)
        self.remessa = remessa  # int(int/remessa)
        self.numero_de_femeas = numero_de_femeas  # int(int)
        self.numero_de_machos = numero_de_machos  # int(int)
