from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

alface_roxo = Plant(
    "Alface roxo",
    0.4 * 1,  # producao da casa
    0,  # valor
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # estacao da colheita
    3,  # tempo de frutificacao
    60 / 4 / 60,  # tempo de colheita
    60 / 6 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0.2,  # custo de muda
    0.4,  # producao por muda
    20,  # remessa
    250,  # max
)
