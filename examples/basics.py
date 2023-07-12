from pyomo.environ import *

model = ConcreteModel()

model.x = Var(within=NonNegativeReals, bounds=(0, 10))
model.y = Var(within=NonNegativeReals, bounds=(0, 10))

model.obj = Objective(expr=3 * model.x + 5 * model.y, sense=maximize)

model.c1 = Constraint(expr=model.x <= 4)
model.c2 = Constraint(expr=2 * model.y <= 12)
model.c3 = Constraint(expr=3 * model.x + 2 * model.y <= 18)

solver = SolverFactory("glpk")

results = solver.solve(model)

print("x=", value(model.x))
print("y=", value(model.y))
print("obj=", value(model.obj))
