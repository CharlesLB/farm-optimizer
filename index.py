# python -u index.py

import sys
from pyomo.environ import *
from core.objective import obj_rule
from core.constraints import (
    plant_rule_producao,
    plant_rule_plantar_o_que_colho,
    rule_trabalhar_mais_que_o_planejado_mes,
    plant_rule_max,
)
from resources.constants.constants import (
    monthsInYear,
)
from resources.data import plants


def print_quantidade_colher_plantar(model):
    for month in months:
        print("\nmonth:", month + 1)
        for plant in plants:
            index: int = plants.index(plant)

            if (
                model.quantidade_plantar[index, month].value
                or model.quantidade_colher[index, month].value
            ):
                print(
                    plant.nome,
                    ": must plant=",
                    value(model.quantidade_plantar[index, month].value),
                    "and must harvest=",
                    value(model.quantidade_colher[index, month].value),
                )


arguments = sys.argv

if arguments.__len__() == 1:
    print("No input file provided")
    print("Usage: python -u index.py <input_file>")
    exit()


model = ConcreteModel()

plantas = list(range(plants.__len__()))
months = list(range(monthsInYear))

model.quantidade_plantar = Var(plantas, months, domain=NonNegativeIntegers)
model.quantidade_colher = Var(plantas, months, domain=NonNegativeReals)

model.obj = Objective(rule=obj_rule, sense=maximize)

model.constraints = ConstraintList()

for plant in plants:
    model.constraints.add(plant_rule_max(model, plant))

    for month in months:
        model.constraints.add(plant_rule_producao(model, month, plant))
        model.constraints.add(plant_rule_plantar_o_que_colho(model, month, plant))

for month in months:
    model.constraints.add(rule_trabalhar_mais_que_o_planejado_mes(model, month))

solver = SolverFactory("glpk")
results = solver.solve(model)

print("obj=", value(model.obj))
print_quantidade_colher_plantar(model)
