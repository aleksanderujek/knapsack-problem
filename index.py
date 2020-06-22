from models.individual import Individual
from models.population import Population
from selections.selection import selection
from crossovers.crossover import crossover
from mutations.mutation import mutation
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

num_of_elements = 10
newIndividual = Individual(num_of_elements)

cost_list = np.full(num_of_elements, [10,15,20,6,3,23,7,11,1,5])
weight_list = np.full(num_of_elements, [10,14,15,3,1,13,3,12,1,10])
max_weight = 40
population_size = 50
generations = 10000

population = Population(population_size,num_of_elements)

def cycle(population, cost_list, weight_list, max_weight, crossover_ratio, mutation_ratio, generationIndex = 0, breakPoint = 50):
    fitness = population.calculate_fitness(cost_list, weight_list, max_weight)
    best = population.get_best()
    selections = selection(population, generationIndex, breakPoint)
    crossovers = crossover(selections, crossover_ratio)
    mutations = mutation(crossovers, mutation_ratio)
    return mutations, fitness, best


fitness_history = np.empty((generations,population_size), dtype=int)

best = Individual(None)

for i in tqdm(range(generations)):
    population, fitness, currentBest = cycle(population, cost_list, weight_list, max_weight, 0.9, 0.4, i,(generations*3)/4)
    if (currentBest.fitness > best.fitness):
        best = currentBest
    fitness_history[i] = fitness


print("================================")
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