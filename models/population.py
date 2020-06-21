import numpy as np
from models.individual import Individual

class Population:
    individuals = []
    best = []
    def __init__(self,population_size,number_of_elements = None):
        if (population_size is not None and number_of_elements is not None):
            self.individuals = np.empty(population_size, dtype=object)
            for i in range(population_size):
                self.individuals[i] = Individual(number_of_elements)

    def calculate_fitness(self, cost_list,weight_list,max_weight):
        shape = self.individuals.shape[0]
        fitness = np.empty(shape, dtype=int)
        for i in range(shape):
            fitness[i] = self.individuals[i].calculate_fitness(cost_list,weight_list, max_weight)
        return fitness

    def get_best(self):
        self.best = max(self.individuals, key = lambda x: x.fitness)
        return self.best