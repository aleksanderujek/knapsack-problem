from models.individual import Individual
from models.population import Population

newIndividual = Individual(10)
print(newIndividual)
print(newIndividual.knapsack)


population = Population(15,10)
print(population)
for element in population.individuals:
    print(element.knapsack)