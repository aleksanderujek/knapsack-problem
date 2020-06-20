from random import randint


def roulette(population):
    return population.individuals[getWinnerInterval(roulettePool(population))]


def getWinnerInterval(individuals):
    rnd = randint(0, individuals[-1])
    winner = 0
    for i in range(0, len(individuals)-1):
        if rnd < individuals[i+1]:
            winner = i
            break
    return winner

def roulettePool(population):
    prev = 0
    pool = [0]
    for individual in population.individuals:
        pool.append(prev + individual.fitness)
        prev += individual.fitness
    return pool