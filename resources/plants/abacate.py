from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

abacate = Plant(
    "abacate",
    60,  # producao da casa
    1,  # valor
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # estacao da colheita
    8,  # tempo de frutificacao
    60 / 10 / 60,  # tempo de colheita
    60 / 3 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0,  # custo de muda -> ele faz, por isso é 0
    300,  # producao por muda
    20,  # remessa
    12,  # max
)
