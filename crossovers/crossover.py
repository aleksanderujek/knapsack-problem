from crossovers.one_point_crossover import one_point_crossover
from models.population import Population
import numpy as np

def crossover(population, crossover_ratio = 0.70):
    shape = population.individuals.shape[0]
    newPopulation = Population(None)
    newPopulation.individuals = np.empty(shape=shape, dtype=object)
    for i in range(shape):
        newPopulation.individuals[i] = one_point_crossover(population.individuals[i],population.individuals[(i+1)%(shape-1)])
    return newPopulation