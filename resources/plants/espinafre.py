from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

espinafre = Plant(
    "Espinafre",
    0.3 * 3,  # producao da casa
    0,  # valor
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # estacao da colheita
    3,  # tempo de frutificação
    60 / 3 / 60,  # tempo de colheita
    60 / 6 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0.2,  # custo de muda
    0.3,  # producao por muda
    20,  # remessa
    250,  # max
)
