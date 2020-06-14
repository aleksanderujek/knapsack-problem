import numpy as np
from models.individual import Individual

class Population:
    individuals = []
    best = []
    def __init__(self,population_size,number_of_elements):
        self.individuals = np.empty(population_size, dtype=object)
        for i in range(population_size):
            self.individuals[i] = Individual(number_of_elements)

    def calculate_fitness(self, cost_list,weight_list,max_weight):
        for individual in self.individuals:
            individual.calculate_fitness(cost_list,weight_list, max_weight)

    def get_best(self):
        self.best = max(self.individuals, key = lambda x: x.fitness)
        return self.best