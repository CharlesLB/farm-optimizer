from pyomo.environ import *
from core.objective import obj_rule
from core.constraints import plant_rule_produção, plant_rule_plantar_o_que_colho
from resources.constants.constants import (
    monthsInTheYear,
)
from resources.plants._all import plants


def print_quantidade_colher_plantar(model):
    for month in months:
        print("\nmonth:", month)
        for plant in plants:
            index: int = plants.index(plant)

            if model.quantidade_plantar[month, index].value:
                print(
                    plant.nome,
                    ": must plant=",
                    value(model.quantidade_plantar[month, index].value),
                    "and must harvest=",
                    value(model.quantidade_colher[month, index].value),
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

model.constraints = ConstraintList()

for month in months:
    for plant in plants:
        model.constraints.add(plant_rule_produção(model, month, plant))
        model.constraints.add(plant_rule_plantar_o_que_colho(model, month, plant))

solver = SolverFactory("glpk")
results = solver.solve(model)

print("obj=", value(model.obj))
print_quantidade_colher_plantar(model)
