from pyomo.environ import *
from resources.constants.constants import (
    monthsInTheYear,
)
from core.objective import obj_rule
from resources.plants._all import plants


def print_quantidade_colher_plantar(model):
    for month in months:
        print("month=", month, "\n")
        for plant in plants:
            index: int = plants.index(plant)

            print(
                "plant=",
                plant.nome,
                "must plant=",
                value(model.quantidade_plantar[month, index]),
                "and must harvest=",
                value(model.quantidade_colher[month, index]),
            )


model = ConcreteModel()

plantas = list(range(plants.__len__()))
months = list(range(monthsInTheYear))

model.quantidade_plantar = Var(months, plantas, domain=NonNegativeReals)
model.quantidade_colher = Var(months, plantas, domain=NonNegativeReals)
model.total_trabalhado_mes_animal = Var(domain=NonNegativeReals)

model.obj = Objective(
    rule=obj_rule,
)


print("obj=", value(model.obj))
print_quantidade_colher_plantar(model)
