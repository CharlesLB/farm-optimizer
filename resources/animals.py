from lib.animal import Animal
from resources.constants import (
    custo_por_animal,
    tempo_de_venda_animal,
    remessa_padrao_de_ovos,
)

galos = Animal(
    "galos",
    40,
    0.83,
    0.0166666666666667,
    custo_por_animal,
    tempo_de_venda_animal,
    0.75,
    remessa_padrao_de_ovos,
    20,
    5,
)

patos = Animal(
    "patos",
    0,
    0.83,
    0.0166666666666667,
    custo_por_animal,
    tempo_de_venda_animal,
    0.5,
    remessa_padrao_de_ovos,
    10,
    10,
)


animals = [galos, patos]
