import numpy as np
from models.individual import Individual

class Population:
    individuals = []

    def __init__(self,population_size,number_of_elements):
        self.individuals = np.empty(population_size, dtype=object)
        for i in range(population_size):
            self.individuals[i] = Individual(number_of_elements)
