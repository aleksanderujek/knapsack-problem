import numpy as np
from selections.tournament import tournament
from selections.roulette import roulette
from models.population import Population

def selection(population, iteration, breakPoint = 50, k = 3):
    shape = population.individuals.shape[0]
    new_population = Population(None)
    new_population.individuals = np.empty(shape=shape, dtype=object)
    for i in range(shape):
        new_population.individuals[i] = roulette(population) if (iteration < breakPoint) else tournament(population)
    return new_population