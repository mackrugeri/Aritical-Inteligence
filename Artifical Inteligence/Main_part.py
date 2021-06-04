import Second_part as Sp
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

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = Sp.breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen,cities):
    popRanked = Sp.rankRoutes(currentGen, cities)
    selectionResults = Sp.selection(popRanked, eliteSize)
    matingpool = Sp.matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

def Algorithm(cities, cityNames):

    weigth = Sp.checkweight(cityNames)    
    for i in range(0, generations):
        weigth = nextGeneration(weigth,cities)

    Index = Sp.rankRoutes(weigth, cities)[0][0]
    ShortestRoute = weigth[Index]
    return ShortestRoute

def dic_making_cities(dic_city):
	for i in range(len(cities)):
		city = {}
		for j in range(len(cities[0])):
			city['city' + str(j+1)] = cities[i][j]
		dic_city['city' + str(i+1)] = city
	return dic_city

def main_start():

	dic_cities= {}
	dic_cities = dic_making_cities(dic_cities)
	cityNames = ['city1','city2','city3','city4','city5','city6','city7','city8','city9','city10']
	Shortest_path = Algorithm( dic_cities, cityNames)
	print(Shortest_path)


main_start()