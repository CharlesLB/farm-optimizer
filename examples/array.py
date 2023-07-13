from pyomo.environ import *

model = ConcreteModel()

n_fabricas = 3
n_clientes = 4

fabricas = list(range(n_fabricas))
clientes = list(range(n_clientes))

ofertas = [75, 125, 100]
demandas = [80, 65, 70, 85]
custos = [[464, 513, 684, 857], [352, 416, 690, 791], [995, 682, 388, 685]]

model.x = Var(fabricas, clientes, domain=NonNegativeIntegers)


def obj_rule(model):
    return sum(custos[i][j] * model.x[i, j] for i in fabricas for j in clientes)


model.obj = Objective(
    rule=obj_rule,
)


def demanda_rule(model, j):
    return sum(model.x[i, j] for i in fabricas) == demandas[j]


model.demanda = ConstraintList()
for j in clientes:
    model.demanda.add(demanda_rule(model, j))


def oferta_rule(model, i):
    return sum(model.x[i, j] for j in clientes) <= ofertas[i]


model.oferta = ConstraintList()
for i in fabricas:
    model.oferta.add(oferta_rule(model, i))

solver = SolverFactory("glpk")
results = solver.solve(model, tee=True)

cost = model.obj.expr()
print("cost=", cost)

for i in fabricas:
    for j in clientes:
        x_value = model.x[i, j].value
        if x_value != 0:
            print("Fábrica %s vende para cliente %s %s unidades" % (i, j, x_value))
