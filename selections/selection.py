import numpy as np
from selections.tournament import tournament
from selections.roulette import roulette
from models.population import Population

def selection(population, iteration, k = 3):
    shape = population.individuals.shape[0]
    new_population = Population(None)
    new_population.individuals = np.empty(shape=shape, dtype=object)
    if (iteration < 50):
        for i in range(shape):
            new_population.individuals[i] = roulette(population)
    else:
        for i in range(shape):
            new_population.individuals[i] = tournament(population)
    return new_population