from pyomo.environ import *

model = ConcreteModel()

# Constants
daysInTheMonth = 30
workDaysInTheMonth = 22

# Sets
limitador_de_ciclos_anos = 10
horas_de_manutencao_por_mes = 40
horas_de_trabalho_por_dia = 6
horas_de_trabalho_por_mes = horas_de_trabalho_por_dia * workDaysInTheMonth

preco_racao_aves = 78.3
numero_de_sacos_por_mes = 3
custo_por_animal = 78.3 * 3 / 45
remessa_padrao_de_ovos = (12 + 24) / 2
tempo_de_venda_planta = 2
tempo_de_venda_animal = 1

model.meses = RangeSet(1, 12)
model.anos = RangeSet(1, limitador_de_ciclos_anos)

model.animal = Set(
    initialize=[
        "producao_da_casa",  # float(int/mês)
        "valor",  # float(R$)
        "tempo_de_cuidado",  # float(horas/dia/animal)
        "custo_por_animal",  # float(R$/mês/animal)
        "tempo_de_venda",  # float(h/remessa)
        "tempo_de_producao",  # float(int/dias)
        "remessa",  # int(int/remessa)
        "numero_de_femeas",  # int(int)
        "numero_de_machos",  # int(int)
    ],
    doc="animais",
)

model.planta = Set(
    initialize=[
        "producao_da_casa",  # float(int/mês)
        "valor",  # float(R$)
        "estacao_da_colheita",  # bool[12]
        "tempo_de_frutificação",  # int(mes)
        "tempo_de_colheita",  # float(h)
        "tempo_de_plantio",  # float(h)
        "tempo_de_venda",  # float(h)
        "custo_de_muda",  # float(R$)
        "producao_por_muda",  # float
        "remessa",  # int(kg)
        "max",  # float(kg)
    ]
)

# Animals Params

model.galos = Param(
    model.animal,
    initialize={
        "producao_da_casa": 40,
        "valor": 0.83,
        "tempo_de_cuidado": 0.0166666666666667,
        "custo_por_animal": custo_por_animal,
        "tempo_de_venda": tempo_de_venda_animal,
        "tempo_de_producao": 0.75,
        "remessa": remessa_padrao_de_ovos,
        "numero_de_femeas": 20,
        "numero_de_machos": 5,
    },
    doc="Dados dos galos",
)

model.patos = Param(
    model.animal,
    initialize={
        "producao_da_casa": 0,
        "valor": 0.83,
        "tempo_de_cuidado": 0.0166666666666667,
        "custo_por_animal": custo_por_animal,
        "tempo_de_venda": tempo_de_venda_animal,
        "tempo_de_producao": 0.5,
        "remessa": remessa_padrao_de_ovos,
        "numero_de_femeas": 10,
        "numero_de_machos": 10,
    },
    doc="Dados dos patos",
)


# Variables

model.lucro = Var(domain=Reals)
model.total_trabalhado_mes_animal = Var(domain=NonNegativeReals)


# Constraints


def trabalhar_mais_que_o_planejado(model):
    return (
        model.galos.tempo_de_cuidado * model.galos.numero_de_femeas
        + (
            model.galos.numero_de_femeas
            * model.galos.tempo_de_producao
            * daysInTheMonth
        )
        / model.galos.remessa
        * model.galos.tempo_de_venda
        <= horas_de_trabalho_por_mes - horas_de_manutencao_por_mes
    )


model.trabalhar_mais_que_o_planejado = Constraint(rule=trabalhar_mais_que_o_planejado)


def cobrir_a_producao_da_casa_animal(model):
    return (
        model.galos.producao_da_casa
        <= model.galos.numero_de_femeas * model.galos.tempo_de_producao * daysInTheMonth
    )


model.cobrir_a_producao_da_casa_animal = Constraint(
    rule=cobrir_a_producao_da_casa_animal
)

# Objective


def obj_rule(model):
    return model.lucro == (
        (
            (
                model.galos.numero_de_femeas
                * model.galos.tempo_de_producao
                * daysInTheMonth
                * limitador_de_ciclos_anos
                * daysInTheMonth
            )
            - model.galos.producao_da_casa
        )
        * model.galos.valor
    ) - (
        (model.galos.numero_de_machos + model.galos.numero_de_femeas)
        * model.galos.custo_por_animal
    )


model.obj = Objective(
    rule=obj_rule,
    sense=maximize,
)

print("obj=", value(model.obj))
