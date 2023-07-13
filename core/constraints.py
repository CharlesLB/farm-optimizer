from pyomo.environ import *
from resources.plants._all import plants
from resources.animals._all import animals
from utils.month import getPlantMonth
from resources.constants.constants import (
    daysInTheMonth,
    horas_de_trabalho_por_mes,
)


# General constraints

months = list(range(12))


def rule_trabalhar_mais_que_o_planejado(model):
    return (
        sum(
            animal.tempo_de_cuidado * animal.numero_de_femeas * daysInTheMonth
            + (animal.numero_de_femeas * animal.tempo_de_produção * daysInTheMonth)
            / animal.remessa
            * animal.tempo_de_venda
        )
        for animal in animals
    ) + (
        sum(
            (
                model.quantidade_colher[month, plants.index(plant)]
                * plant.tempo_de_colheita
            )
            + (
                model.quantidade_plantar[month, plants.index(plant)]
                * plant.tempo_de_plantio
            )
            + (
                (
                    model.quantidade_colher[month, plants.index(plant)]
                    - plant.produção_da_casa
                )
                / plant.remessa
                * plant.tempo_de_venda
            )
        )
        for month in months
        for plant in plants
    ) <= horas_de_trabalho_por_mes


# Plant constraints


def plant_rule_produção(model, month, plant):
    return (
        model.quantidade_colher[month, plants.index(plant)]
        >= plant.produção_da_casa * plant.estação_da_colheita[month]
    )


def plant_rule_plantar_o_que_colho(model, month, plant):
    return (
        model.quantidade_plantar[month, plants.index(plant)]
        <= model.quantidade_colher[
            getPlantMonth(month, plant.tempo_de_frutificação), plants.index(plant)
        ]
        * plant.produção_por_muda
    )


# model.animal_constraints = ConstraintList()

# for animal in animals:
#     model.animal_constraints.add(animal_rule_produção(model, animal))
#     model.animal_constraints.add(
#         animal_rule_trabalhar_mais_que_o_planejado(model, animal)
#     )


# def general_rule_trabalhar_mais_que_o_planejado(model):
#     return (
#         model.total_trabalhado_mes_animal
#         <= horas_de_trabalho_por_mes - horas_de_manutencao_por_mes
#     )


# model.general_constraint = Constraint(
#     rule=general_rule_trabalhar_mais_que_o_planejado,
# )
