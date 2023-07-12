from pyomo.environ import *

# Create a concrete optimization model
model = ConcreteModel()

# Define the index sets
model.I = RangeSet(1, 10)  # Replace num_i with the appropriate range for i
model.J = RangeSet(1, 12)  # Replace num_j with the appropriate range for j

# Define the decision variable
model.q = Var(model.I, model.J, within=NonNegativeReals)

# Define the objective function
model.obj = Objective(expr=sum_product(model.q), sense=maximize)

# Define the constraint
model.constraint = Constraint(
    model.I,
    model.J,
    rule=lambda model, i, j: model.q[i, j] >= model.I[i] * model.J[i, j],
)

solver = SolverFactory("glpk")
results = solver.solve(model)

# Print the optimal solution
if (
    results.solver.status == SolverStatus.ok
    and results.solver.termination_condition == TerminationCondition.optimal
):
    print("Optimal Solution Found")
    print("Objective Value:", model.obj())
    print("Decision Variables:")
    for i in model.I:
        for j in model.J:
            print("q[{}, {}]: {}".format(i, j, model.q[i, j]()))
else:
    print("Solver did not find an optimal solution")
