from pyomo.environ import *
from resources.animals import animals
from resources.constants import (
    horas_de_trabalho_por_mes,
    horas_de_manutencao_por_mes,
    daysInTheMonth,
    limitador_de_ciclos_anos,
)

model = ConcreteModel()

# Variables

model.lucro = Var(domain=Reals)
model.total_trabalhado_mes_animal = Var(domain=NonNegativeReals)


# Constraints


model.trabalhar_mais_que_o_planejado = Constraint(
    expr=model.galos["tempo_de_cuidado"] * model.galos["numero_de_femeas"]
    + (
        model.galos["numero_de_femeas"]
        * model.galos["tempo_de_producao"]
        * daysInTheMonth
    )
    / model.galos["remessa"]
    * model.galos["tempo_de_venda"]
    <= horas_de_trabalho_por_mes - horas_de_manutencao_por_mes
)


model.cobrir_a_producao_da_casa_animal = Constraint(
    expr=model.galos["producao_da_casa"]
    <= model.galos["numero_de_femeas"]
    * model.galos["tempo_de_producao"]
    * daysInTheMonth
)

# Objective


def obj_rule(model):
    return model.lucro == (
        (
            (
                model.galos["numero_de_femeas"]
                * model.galos["tempo_de_producao"]
                * daysInTheMonth
                * limitador_de_ciclos_anos
                * daysInTheMonth
            )
            - model.galos["producao_da_casa"]
        )
        * model.galos.valor
    ) - (
        (model.galos["numero_de_machos"] + model.galos["numero_de_femeas"])
        * model.galos["custo_por_animal"]
    )


model.obj = Objective(
    rule=obj_rule,
    sense=maximize,
)

print("obj=", value(model.obj))
