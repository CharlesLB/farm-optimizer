from pyomo.environ import *
from core.objective import obj_rule
from core.constraints import (
    plant_rule_produção,
    plant_rule_plantar_o_que_colho,
    rule_trabalhar_mais_que_o_planejado,
)
from resources.constants.constants import (
    monthsInTheYear,
)
from resources.plants._all import plants


def print_quantidade_colher_plantar(model):
    for month in months:
        print("\nmonth:", month)
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


model = ConcreteModel()

plantas = list(range(plants.__len__()))
months = list(range(monthsInTheYear))

model.quantidade_plantar = Var(plantas, months, domain=NonNegativeIntegers)
model.quantidade_colher = Var(plantas, months, domain=NonNegativeReals)

model.obj = Objective(
    rule=obj_rule,
)

model.constraints = ConstraintList()

for plant in plants:
    for month in months:
        model.constraints.add(plant_rule_produção(model, month, plant))
        model.constraints.add(plant_rule_plantar_o_que_colho(model, month, plant))

model.constraints.add(rule_trabalhar_mais_que_o_planejado(model))

solver = SolverFactory("glpk")
results = solver.solve(model)

print("obj=", value(model.obj))
print_quantidade_colher_plantar(model)
