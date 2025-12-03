import time
start = time.process_time()

import re
import random
Input = open('Input.txt','r').read().splitlines()
for i in range(len(Input)):
    Input[i] = re.split(' |,',Input[i])
    for j in reversed(range(len(Input[i]))):
        if not(Input[i][j].isnumeric()) and not('-' in Input[i][j]):
            Input[i].pop(j)
    for j in range(len(Input[i])):
        Input[i][j] = int(Input[i][j])
def calculateCookieScore(ingredientAmounts):
    sums = [0]*5
    for i in range(5):
        for j in range(len(ingredientAmounts)):
            sums[i] = sums[i] + Input[j][i]*ingredientAmounts[j]
    multiply = 1
    for i in range(len(sums)):
        if sums[i]<=0 or not(sums[4] == 500):
            return 0
        else:
            multiply = multiply*sums[i]
    return multiply/500
def findChanges(inList):
    outList = []
    for i in range(len(inList)):
        for j in range(len(inList)):
            addList = []
            for k in range(len(inList)):
                if not(j==i):
                    if k == i:
                        addList.append(inList[k]+1)
                    elif k == j:
                        addList.append(inList[k]-1)
                    else:
                        addList.append(inList[k])
                else:
                    addList.append(inList[k])
            if outList.count(addList) == 0 and addList.count(101) == 0 and addList.count(-1) == 0:
                outList.append(addList)
    scores = []
    for i in outList:
        scores.append(calculateCookieScore(i))
    return outList[scores.index(max(scores))]
totalTablespoons = 100
def generateAmounts():
    outList = []
    highest = totalTablespoons
    for i in range(len(Input)-1):
        outList.append(random.randint(0,highest))
        highest = highest - outList[i]
    outList.append(highest)
    return outList
tries = []
for i in range(100000):
    amountsPerIngrediant = generateAmounts()
    previousScore = calculateCookieScore(amountsPerIngrediant)
    newScoreAmounts = findChanges(amountsPerIngrediant)
    newScore = calculateCookieScore(newScoreAmounts)
    while newScore>previousScore:
        previousScore = newScore
        previousIngrediants = newScoreAmounts
        newScoreAmounts = findChanges(previousIngrediants)
        newScore = calculateCookieScore(newScoreAmounts)
    tries.append(newScore)
print(max(tries))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[29] = '2015|Day 15|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()