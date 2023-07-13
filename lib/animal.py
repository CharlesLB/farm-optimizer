class Animal:
    def __init__(
        self,
        nome,
        producao_da_casa,
        valor,
        tempo_de_cuidado,
        custo_por_animal,
        tempo_de_venda,
        tempo_de_producao,
        remessa,
        numero_de_femeas,
        numero_de_machos,
    ):
        self.nome = nome
        self.producao_da_casa = producao_da_casa  # float(int/mês)
        self.valor = valor  # float(R$)
        self.tempo_de_cuidado = tempo_de_cuidado  # float(horas/dia/animal)
        self.custo_por_animal = custo_por_animal  # float(R$/mês/animal)
        self.tempo_de_venda = tempo_de_venda  # float(h/remessa)
        self.tempo_de_producao = tempo_de_producao  # float(int/dias)
        self.remessa = remessa  # int(int/remessa)
        self.numero_de_femeas = numero_de_femeas  # int(int)
        self.numero_de_machos = numero_de_machos  # int(int)
