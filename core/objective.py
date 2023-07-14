from pyomo.environ import *
from resources.data import plants
from resources.data import animals
from resources.constants.constants import daysInTheYear, monthsInYear

months = list(range(12))


def obj_rule_plants(model):
    return sum(
        (
            (
                model.quantidade_colher[plants.index(plant), month]
                * plant.estacao_da_colheita[month]
            )
            - (plant.producao_da_casa * plant.estacao_da_colheita[month])
        )
        * plant.valor
        for plant in plants
        for month in months
    )


def obj_rule_animals(model):
    return sum(
        (
            (
                (
                    (animal.numero_de_femeas * animal.tempo_de_producao * daysInTheYear)
                    - animal.producao_da_casa * monthsInYear
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
