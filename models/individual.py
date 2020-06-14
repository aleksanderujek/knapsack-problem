import numpy as np

class Individual:
    knapsack = np.array([])
    fitness = 0
    weight = 0

    def __init__(self, n):
        self.knapsack = np.random.choice([False, True], size=n)
        
    def num_of_elements(self):
        return np.sum(self.knapsack)

    def calculate_fitness(self, cost_list, weight_list, max_weight):
        fitness = np.dot(self.knapsack, cost_list)
        num_of_elements = self.num_of_elements()
        weight = self.calculate_weight(weight_list)
        if (num_of_elements % 2 != 0 or num_of_elements == 0 or weight > max_weight):
            self.fitness = -1
        else:
            self.fitness =fitness
        return self.fitness

    def calculate_weight(self, weight_list):
        self.weight = np.dot(self.knapsack, weight_list)
        return self.weight