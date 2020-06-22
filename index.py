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
population_size = 200
generations = 1000

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
best_generation = 0

for i in tqdm(range(generations)):
    population, fitness, currentBest = cycle(population, cost_list, weight_list, max_weight, 0.9, 0.6, i,(generations*3)/4)
    if (currentBest.fitness > best.fitness):
        best = currentBest
        best_generation = i
    fitness_history[i] = fitness


print("================================")
print("Best found at \33[93m{0}\x1b[0m generation".format(best_generation))
print("Fitness: \33[92m{0}\x1b[0m".format(best.fitness))
print("Knapsack: \33[94m{0}\x1b[0m".format(best.knapsack))
print("Number of elements in knapsack: \33[90m{0}\x1b[0m".format(best.num_of_elements()))
print("Knapsack weight: \33[91m{0}\x1b[0m".format(best.weight))
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