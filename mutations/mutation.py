from random import random
from mutations.bit_flip_mutation import bit_flip_mutation

def mutation(population, mutationRate=0.05):
    for individual in population.individuals:
        randomValue = random()
        individual = bit_flip_mutation(individual) if mutationRate>randomValue else individual
    return population