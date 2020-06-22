from random import randint

def inversion_mutation(individual):
    length = len(individual.knapsack)
    start_point = randint(0, length)
    end_point = randint(start_point, length)
    individual.knapsack[start_point:end_point] = reversed(individual.knapsack[start_point:end_point])
    return individual