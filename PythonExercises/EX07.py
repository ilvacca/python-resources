# Esercizio 7
# Throwing dices

import random

launches = 36000

launchesList = [[random.randint(1,6) for i in range(2)] for j in range(launches)]
print(launchesList)

launchesSum = [sum(row) for row in launchesList]
print(launchesSum)

count = {}

for c in range(len(launchesSum)):
    if (launchesSum[c] in count):
        count[launchesSum[c]]+=1
    else:
        count[launchesSum[c]]=1

print(count)
