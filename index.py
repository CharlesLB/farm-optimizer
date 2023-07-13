from pyomo.environ import *
from resources.animals import Animal

model = ConcreteModel()

animal = Animal("galos", 1)

print(animal.name)
print(animal.age)
