# Exercise 6

import random

numbersList = [random.randint(1,100) for i in range(10)]

index = len(numbersList)-1 
resultList = []

while index:
    resultList.append(numbersList[index])
    index-=1
resultList.append(numbersList[0])

print(resultList)
