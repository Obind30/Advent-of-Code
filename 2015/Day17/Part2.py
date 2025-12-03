import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = int(Input[i])
def sameList(list1, list2):
    if not(len(list1) == len(list2)):
        return False
    retBool = True
    for i in range(len(list1)):
        if not(list1.count(list1[i]) == list2.count(list1[i])):
            retBool = False
    return retBool
def combinationsThatAddTo(x,indicies, usedIndicies):
    if x == 0:
        return [usedIndicies]
    else:
        out = []
        toUse = indicies.copy()
        i = 0
        while len(toUse)>0:
            if x-Input[toUse[i]]>=0:
                nextIndicies = toUse.copy()
                nextIndicies.pop(0)
                recurs = combinationsThatAddTo(x-Input[toUse[i]],nextIndicies,usedIndicies+[toUse[i]])
            else:
                recurs = []
            toUse.pop(0)
            out = out + recurs 
        return out
IndiciesList = [item for item in range(0, len(Input))]
combos = combinationsThatAddTo(150,IndiciesList,[])
numLength = float('inf')
sum = 0
for i in combos:
    if len(i)<numLength:
        sum = 1
        numLength = len(i)
    elif len(i) == numLength:
        sum =sum + 1
print(sum)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[33] = '2015|Day 17|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()