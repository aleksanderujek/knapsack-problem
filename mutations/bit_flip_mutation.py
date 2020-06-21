from random import randint

def bit_flip_mutation(individual):
    index = randint(0, len(individual.knapsack)-1)
    individual.knapsack[index] = not individual.knapsack[index]
    return individual