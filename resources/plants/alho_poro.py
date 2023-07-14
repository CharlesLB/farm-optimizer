from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

alho_poró = Plant(
    "Alho poró",
    1 * 5,  # producao da casa
    0,  # valor
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # estacao da colheita
    5,  # tempo de frutificacao
    60 / 5 / 60,  # tempo de colheita
    60 / 8 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0.2,  # custo de muda
    1,  # producao por muda
    20,  # remessa
    250,  # max
)
