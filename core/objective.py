from pyomo.environ import *
from resources.plants._all import plants
from resources.animals._all import animals
from resources.constants.constants import (
    daysInTheYear,
)

months = list(range(12))


def obj_rule_plants(model):
    return sum(
        (
            model.quantidade_colher[month, plants.index(plant)]
            * plant.estação_da_colheita[month]
        )
        - (plant.produção_da_casa * plant.estação_da_colheita[month]) * plant.valor
        for month in months
        for plant in plants
    )


def obj_rule_animals(model):
    return sum(
        (
            (
                (
                    (animal.numero_de_femeas * animal.tempo_de_produção * daysInTheYear)
                    - animal.produção_da_casa
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
    return obj_rule_animals(model) + obj_rule_plants(model)
