import numpy as np

class Individual:
    knapsack = np.array([])


    def __init__(self, n):
        self.knapsack = np.random.choice([False, True], size=n)
        
