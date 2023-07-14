from lib.plant import Plant
from resources.data import tempo_de_venda_planta

morango = Plant(
    "morango",
    0.8,  # producao da casa
    0,  # valor
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # estacao da colheita
    3,  # tempo de frutificacao
    60 / 4 / 60,  # tempo de colheita
    60 / 8 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0,  # custo de muda -> ele faz, por isso é 0
    0.8,  # producao por muda
    20,  # remessa
    250,  # max
)
