from pyomo.environ import *
from resources.data import (
    plants,
    animals,
    daysInMonth,
    horas_de_trabalho_por_mes,
    monthsInYear,
)
from utils.date import get_plant_month
from utils.math import get_int_value


# General constraints

months = list(range(12))


def rule_trabalhar_mais_que_o_planejado_mes(model, month):
    return (
        (
            sum(
                get_int_value(
                    animal.tempo_de_cuidado * animal.numero_de_femeas * daysInMonth
                    + (animal.numero_de_femeas * animal.tempo_de_producao * daysInMonth)
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
                        - (plant.producao_da_casa * plant.estacao_da_colheita[month])
                    )
                    / plant.remessa
                    * plant.tempo_de_venda
                )
                for plant in plants
            )
        )
    ) <= horas_de_trabalho_por_mes


# Plant constraints


def plant_rule_producao(model, month, plant):
    return (
        model.quantidade_colher[plants.index(plant), month]
        >= plant.producao_da_casa * plant.estacao_da_colheita[month]
    )


def plant_rule_plantar_o_que_colho(model, month, plant):
    return (
        model.quantidade_colher[plants.index(plant), month]
        <= model.quantidade_plantar[
            plants.index(plant), get_plant_month(month, plant.tempo_de_frutificacao)
        ]
        * plant.producao_por_muda
    )


def plant_rule_max(model, plant):
    months = list(range(monthsInYear))
    return (
        sum(model.quantidade_plantar[plants.index(plant), month] for month in months)
        <= plant.max
    )
