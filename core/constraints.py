from pyomo.environ import *

# def animal_rule_producao(model, animal):
#     return (
#         animal.producao_da_casa
#         <= animal.numero_de_femeas * animal.tempo_de_producao * daysInTheMonth
#     )


# def animal_rule_trabalhar_mais_que_o_planejado(model, animal):
#     return (
#         animal.tempo_de_cuidado * animal.numero_de_femeas
#         + (animal.numero_de_femeas * animal.tempo_de_producao * daysInTheMonth)
#         / animal.remessa
#         * animal.tempo_de_venda
#         <= model.total_trabalhado_mes_animal
#     )


# model.animal_constraints = ConstraintList()

# for animal in animals:
#     model.animal_constraints.add(animal_rule_producao(model, animal))
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
