from lib.plant import Plant
from resources.constants.constants import tempo_de_venda_planta

cana_de_açúcar = Plant(
    "cana-de-açúcar",
    10,  # producao da casa
    1,  # valor
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # estacao da colheita
    18,  # tempo de frutificacao
    60 / 12 / 60,  # tempo de colheita
    60 / 3 / 60,  # tempo de plantio
    tempo_de_venda_planta,  # tempo de venda
    0,  # custo de muda -> ele faz, por isso é 0
    300,  # producao por muda
    15,  # remessa
    12,  # max
)
