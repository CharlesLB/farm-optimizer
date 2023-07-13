from pyomo.environ import *
from resources.plants._all import plants
from resources.animals._all import animals
from resources.constants.constants import (
    daysInTheYear,
)


def obj_rule_plants(model):
    return sum((0 * plant.valor) for plant in plants)


def obj_rule_animals():
    return sum(
        (
            (
                (
                    (animal.numero_de_femeas * animal.tempo_de_producao * daysInTheYear)
                    - animal.producao_da_casa
                )
                * animal.valor
            )
            - (
                (animal.numero_de_femeas + animal.numero_de_machos)
                * animal.custo_por_animal
            )
        )
        for animal in animals
    )


def obj_rule(model):
    return obj_rule_animals()
