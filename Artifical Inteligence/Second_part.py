import numpy as np, random, pandas as pd

cities=[
    [0,    60,    25,  350,  400,   20,   70,   65,  150,  700 ],
    [60,    10,    40,  150,   46,   55,   45,   95,   48,  50  ],
    [20,   32,     0,  500,  450,  846,  920,   45,   10,  135 ],
    [30, 110,   410,    80,   15,  178,  832,  204,  256,  250 ],
    [500,  36,   448,   65,    0,  258,  143,  325,  125,  39  ],
    [ 26,  65,   846,  478,  258,    0,  369,  256,  345, 110  ],
    [ 77,  85,   910,  432,  143,  369,    0,   45,  120, 289  ],
    [ 69,  90,    47,  214,  325,  256,   45,    0,  325, 981  ],
    [125,  44,    11,  356,  125,  345,  120,  325,    0, 326  ],
    [650,  54,   145,  251,   39,  110,  289,  981,  326,   0  ],
]

popSize = 50
eliteSize = 5
mutationRate = 0.02
generations = 400


def checkweight(cities):
	Weight = []
	for i in range(popSize):
		we = random.sample(cities, len(cities))
		Weight.append(we)
	return Weight


def calculateFitness(population, cities):
    distance = 0
    
    for i in range(1, len(population)):
        distance += cities[population[i-1]][population[i]]
    
    return distance


def rankRoutes(population, cities):
    res = []
    
    for i in range(len(population)):
        res.append([calculateFitness(population[i], cities), i])
    
    a =  sorted(res, reverse=True)
    for i in range(len(a)):
        a[i][0],a[i][1] = a[i][1],a[i][0]
    return a


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child