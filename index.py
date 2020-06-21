from models.individual import Individual
from models.population import Population
from selections.selection import selection
from crossovers.crossover import crossover
from mutations.mutation import mutation
import numpy as np

newIndividual = Individual(10)


cost_list = np.full(10, [1,2,3,4,5,6,7,8,9,10])
weight_list = np.full(10, [1,2,1,2,1,2,1,2,1,2])
max_weight = 10
num_of_elements = 10
population_size = 16
generations = 100

population = Population(population_size,num_of_elements)
# population.calculate_fitness(cost_list, weight_list, max_weight)
# for i, element in enumerate(population.individuals):
#     print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}").format(i, element.knapsack, element.num_of_elements(), element.fitness, element.weight)

# print("================================")
# best = population.get_best()
# print("Best: {0}, NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}").format(best.knapsack, best.num_of_elements(), best.fitness, best.weight)
# print("================================")


# selections = selection(population, 0)
# for i, element in enumerate(selections.individuals):
#     print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}").format(i, element.knapsack, element.num_of_elements(), element.fitness, element.weight)

# crossovers = crossover(selections)

# for i, element in enumerate(crossovers.individuals):
#     print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}").format(i, element.knapsack, element.num_of_elements(), element.calculate_fitness(cost_list,weight_list, max_weight)
# , element.weight)

# mutations = mutation(crossovers)

def cycle(population, cost_list, weight_list, max_weight, crossover_ratio, mutation_ratio, generationIndex = 0):
    fitness = population.calculate_fitness(cost_list, weight_list, max_weight)
    selections = selection(population, generationIndex)
    crossovers = crossover(selections, crossover_ratio)
    mutations = mutation(crossovers, mutation_ratio)
    return mutations, fitness


result, result2 = cycle(population, cost_list, weight_list, max_weight, 0.70, 0.05, 0)

fitness_history = np.empty((generations,population_size), dtype=int)



for i in range(generations):
    population, fitness = cycle(population, cost_list, weight_list, max_weight, 0.70, 0.05, i)
    fitness_history[i] = fitness

population.calculate_fitness(cost_list, weight_list, max_weight)
for i, element in enumerate(population.individuals):
    print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}").format(i, element.knapsack, element.num_of_elements(), element.fitness, element.weight)

print("================================")
best = population.get_best()
print("Best: {0}, NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}").format(best.knapsack, best.num_of_elements(), best.fitness, best.weight)
print("================================")
