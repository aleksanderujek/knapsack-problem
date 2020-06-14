from models.individual import Individual
from models.population import Population
import numpy as np

newIndividual = Individual(10)
print(newIndividual)
print(newIndividual.knapsack)


cost_list = np.full(10, [1,2,3,4,5,6,7,8,9,10])
weight_list = np.full(10, [1,2,1,2,1,2,1,2,1,2])
max_weight = 10
num_of_elements = 10
population_size = 15

population = Population(population_size,num_of_elements)
population.calculate_fitness(cost_list, weight_list, max_weight)
for i, element in enumerate(population.individuals):
    print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}").format(i, element.knapsack, element.num_of_elements(), element.fitness, element.weight)

print("================================")
best = population.get_best()
print("Best: {0}, NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}").format(best.knapsack, best.num_of_elements(), best.fitness, best.weight)
print("================================")