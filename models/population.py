import numpy as np
from models.individual import Individual

class Population:
    individuals = []
    best = []
    def __init__(self,population_size,number_of_elements):
        self.individuals = np.empty(population_size, dtype=object)
        for i in range(population_size):
            self.individuals[i] = Individual(number_of_elements)

    def get_best(self, cost_list, weight_list, max_weight):
        self.best = max(self.individuals, key = lambda x: x.calculate_fitness(cost_list,weight_list,max_weight))
        return self.best