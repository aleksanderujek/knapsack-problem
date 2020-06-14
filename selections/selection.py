import numpy as np
from selections.tournament import tournament

def selection(population, iteration, k = 3):
    shape = population.individuals.shape[0]
    new_population = np.empty(shape=shape, dtype=object)
    if (iteration < 50):
        for i in range(shape):
            new_population[i] = tournament(population)
    else:
        for i in range(shape):
            new_population[i] = tournament(population)
    return new_population