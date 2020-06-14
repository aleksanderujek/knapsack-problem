from models.individual import Individual
from models.population import Population
import numpy as np

newIndividual = Individual(10)
print(newIndividual)
print(newIndividual.knapsack)


cost_list = np.full(10, [1,2,3,4,5,6,7,8,9,10])
weight_list = np.full(10, [1,2,1,2,1,2,1,2,1,2])
max_weight = 10

population = Population(15,10)
print(population)
for element in population.individuals:
    print("TABLE: {0}  NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}").format(element.knapsack, element.num_of_elements(), element.calculate_fitness(cost_list, weight_list, max_weight), element.weight)

print("================================")
best = population.get_best(cost_list, weight_list, max_weight)
print("Best: {0}, NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}").format(best.knapsack, best.num_of_elements(), best.fitness, best.weight)
print("================================")