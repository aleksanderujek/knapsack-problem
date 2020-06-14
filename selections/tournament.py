import numpy as np

def tournament(population, k = 3):
    elements = np.random.choice(population.individuals, k)
    return max(elements, key=lambda x: x.fitness)