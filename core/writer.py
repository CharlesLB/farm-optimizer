import time
from pyomo.environ import *
from resources.data import plants, animals, monthsInYear, daysInMonth
from utils.math import get_int_value, float_to_cash
from utils.date import convert_float_to_hour
import csv


months = list(range(monthsInYear))
months_names = [
    "jan",
    "fev",
    "mar",
    "abr",
    "mai",
    "jun",
    "jul",
    "ago",
    "set",
    "out",
    "nov",
    "dez",
]

data_csv = []


def get_quantidade_de_trabalho_por_mes(model, month):
    return (
        sum(
            get_int_value(
                animal.tempo_de_cuidado * animal.numero_de_femeas * daysInMonth
                + (animal.numero_de_femeas * animal.tempo_de_producao * daysInMonth)
                / animal.remessa
            )
            * animal.tempo_de_venda
            for animal in animals
        )
    ) + (
        sum(
            (
                value(model.quantidade_colher[plants.index(plant), month])
                * plant.tempo_de_colheita
            )
            + (
                value(model.quantidade_plantar[plants.index(plant), month])
                * plant.tempo_de_plantio
            )
            + (
                (
                    value(model.quantidade_colher[plants.index(plant), month])
                    - (plant.producao_da_casa * value(plant.estacao_da_colheita[month]))
                )
                / plant.remessa
                * plant.tempo_de_venda
            )
            for plant in plants
        )
    )


def get_lucro_mensal_com_animal(animal):
    return (
        (
            (animal.numero_de_femeas * animal.tempo_de_producao * daysInMonth)
            - animal.producao_da_casa
        )
        * animal.valor
    ) - ((animal.numero_de_femeas + animal.numero_de_machos) * animal.custo_por_animal)


def get_lucro_mensal_com_animais():
    return sum(get_lucro_mensal_com_animal(animal) for animal in animals)


def write_quantidade_colher_plantar(model):
    data_csv.append(["Quantidade de plantas a colher e plantar por mês"])

    header = [
        "Mês",
        "Planta",
        "Quantidade a plantar (Mudas)",
        "Quantidade a colher (Kg)",
    ]

    data_csv.append(header)

    for month in months:
        data_csv.append([months_names[month]])

        for plant in plants:
            index: int = plants.index(plant)

            if (
                model.quantidade_plantar[index, month].value
                or model.quantidade_colher[index, month].value
            ):
                data_csv.append(
                    [
                        "",
                        plant.nome,
                        value(model.quantidade_plantar[index, month].value),
                        value(model.quantidade_colher[index, month].value),
                    ]
                )

        data_csv.append([])

    data_csv.append([])


def write_lucro_mensal_com_animais():
    data_csv.append(["Lucro mensal com animais"])

    header = [
        "Animal",
        "Lucro mensal",
    ]

    data_csv.append(header)

    for animal in animals:
        new_line = [
            animal.nome,
            float_to_cash(get_lucro_mensal_com_animal(animal)),
        ]

        data_csv.append(new_line)


def get_lucro_mensal_com_plantas(model, month):
    return sum(
        (value(model.quantidade_colher[plants.index(plant), month]) * plant.valor)
        - (
            value(model.quantidade_plantar[plants.index(plant), month])
            * plant.custo_de_muda
        )
        for plant in plants
    )


def write_lucro(model):
    data_csv.append(["Informações Gerais"])

    header = [
        "Mês",
        "Total Trabalhado",
        "Total Lucro",
    ]

    data_csv.append(header)

    for month in months:
        data_csv.append(
            [
                months_names[month],
                convert_float_to_hour(get_quantidade_de_trabalho_por_mes(model, month)),
                float_to_cash(
                    get_lucro_mensal_com_plantas(model, month)
                    + get_lucro_mensal_com_animais(),
                ),
            ]
        )

    data_csv.append([])


def write_output(model):
    filename = f"data_output_{time.time()}.csv"

    write_lucro(model)
    write_quantidade_colher_plantar(model)
    write_lucro_mensal_com_animais()

    with open(filename, "w", newline="") as file:
        printer = csv.writer(file)
        printer.writerows(data_csv)
