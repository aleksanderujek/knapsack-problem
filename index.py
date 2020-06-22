from models.individual import Individual
from models.population import Population
from selections.selection import selection
from crossovers.crossover import crossover
from mutations.mutation import mutation
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

newIndividual = Individual(10)


cost_list = np.full(10, [1,2,3,4,5,6,7,8,9,10])
weight_list = np.full(10, [1,2,1,2,1,2,1,2,1,2])
max_weight = 10
num_of_elements = 10
population_size = 100
generations = 1000

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

def cycle(population, cost_list, weight_list, max_weight, crossover_ratio, mutation_ratio, generationIndex = 0, breakPoint = 50):
    fitness = population.calculate_fitness(cost_list, weight_list, max_weight)
    selections = selection(population, generationIndex, breakPoint)
    crossovers = crossover(selections, crossover_ratio)
    mutations = mutation(crossovers, mutation_ratio)
    return mutations, fitness


fitness_history = np.empty((generations,population_size), dtype=int)



for i in tqdm(range(generations)):
    population, fitness = cycle(population, cost_list, weight_list, max_weight, 0.9, 0.7, i,(generations*3)/4)
    fitness_history[i] = fitness

population.calculate_fitness(cost_list, weight_list, max_weight)
for i, element in enumerate(population.individuals):
    print("{0} TABLE: {1}  NUM_OF_ELEMENTS: {2} FITNESS: {3} WEIGHT: {4}".format(i, element.knapsack, element.num_of_elements(), element.fitness, element.weight))

print("================================")
best = population.get_best()
print("Best: {0}, NUM_OF_ELEMENTS: {1} FITNESS: {2} WEIGHT: {3}".format(best.knapsack, best.num_of_elements(), best.fitness, best.weight))
print("================================")



fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]
fitness_history_max = [np.max(fitness) for fitness in fitness_history]
plt.plot(list(range(generations)), fitness_history_mean, label = 'Mean Fitness')
plt.plot(list(range(generations)), fitness_history_max, label = 'Max Fitness')
plt.legend()
plt.title('Fitness through the generations')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()