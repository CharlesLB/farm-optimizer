from pyomo.environ import *
from resources.plants._all import plants
from resources.animals._all import animals
from utils.month import getPlantMonth
from utils.math import getIntValue
from resources.constants.constants import (
    daysInMonth,
    horas_de_trabalho_por_mes,
    monthsInYear,
)


# General constraints

months = list(range(12))


def rule_trabalhar_mais_que_o_planejado_mes(model, month):
    return (
        (
            sum(
                getIntValue(
                    animal.tempo_de_cuidado * animal.numero_de_femeas * daysInMonth
                    + (animal.numero_de_femeas * animal.tempo_de_produção * daysInMonth)
                    / animal.remessa
                )
                * animal.tempo_de_venda
                for animal in animals
            )
        )
        + (
            sum(
                (
                    model.quantidade_colher[plants.index(plant), month]
                    * plant.tempo_de_colheita
                )
                + (
                    model.quantidade_plantar[plants.index(plant), month]
                    * plant.tempo_de_plantio
                )
                + (
                    (
                        model.quantidade_colher[plants.index(plant), month]
                        - (plant.produção_da_casa * plant.estação_da_colheita[month])
                    )
                    / plant.remessa
                    * plant.tempo_de_venda
                )
                for plant in plants
            )
        )
    ) <= horas_de_trabalho_por_mes


# Plant constraints


def plant_rule_produção(model, month, plant):
    return (
        model.quantidade_colher[plants.index(plant), month]
        >= plant.produção_da_casa * plant.estação_da_colheita[month]
    )


def plant_rule_plantar_o_que_colho(model, month, plant):
    return (
        model.quantidade_colher[plants.index(plant), month]
        <= model.quantidade_plantar[
            plants.index(plant), getPlantMonth(month, plant.tempo_de_frutificação)
        ]
        * plant.produção_por_muda
    )


def plant_rule_max(model, plant):
    months = list(range(monthsInYear))
    return (
        sum(model.quantidade_plantar[plants.index(plant), month] for month in months)
        <= plant.max
    )
