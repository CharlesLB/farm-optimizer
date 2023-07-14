from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

maracujá = Plant(
    "Maracujá",
    10,  # producao da casa
    4,  # valor
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # estacao da colheita
    8,  # tempo de frutificacao
    60 / 10 / 60,  # tempo de colheita
    0.4,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0,  # custo de muda -> ele faz, por isso é 0
    25,  # producao por muda
    25,  # remessa
    25 * 30,  # max
)
