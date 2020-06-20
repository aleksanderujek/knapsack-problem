from random import randint
import numpy as np
from models.individual import Individual


def one_point_crossover(parent1, parent2):
    child = Individual(None)
    point = randint(0, len(parent2.knapsack)-1)
    startSet = parent1.knapsack[:point]
    endSet = parent1.knapsack[point:]
    child.knapsack = np.concatenate([startSet,endSet])
    return child