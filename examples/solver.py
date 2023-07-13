from pyomo.environ import *

model = ConcreteModel()
x = 5
y = 3

model.obj = Objective(expr=x * y, sense=maximize)

model.c1 = Constraint(expr=x + y <= 6)

solver = SolverFactory("glpk")

results = solver.solve(model)

print("obj=", value(model.obj))
