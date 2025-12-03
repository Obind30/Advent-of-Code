import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
names = []
for i in range(len(Input)):
    Input[i] = Input[i].split()
    for j in reversed(range(4,10)):
        Input[i].pop(j)
    Input[i].pop(1)
    if Input[i][1] == 'lose':
        Input[i][2] = -1*int(Input[i][2])
    else:
        Input[i][2] = int(Input[i][2])
    Input[i].pop(1)
    if names.count(Input[i][0]) == 0:
        names.append(Input[i][0])
def findPermutations(parentHistory, openList):
    if len(openList) == 1:
        return [parentHistory + [openList[0]]]
    out = []
    for i in openList:
        appenList = [] #maybe fix this
        for j in openList:
            if not(i == j):
                appenList.append(j)
        out = out + findPermutations(parentHistory+[i], appenList)
    return out 
permutations = findPermutations([], names)
maxHappieness = 0
def findScore(firstPerson, secondPerson):
    tempNames = names.copy()
    tempNames.remove(firstPerson)
    return Input[(names.index(firstPerson)*(len(names)-1))+tempNames.index(secondPerson)][1]
for i in permutations:
    happieness = 0
    for j in range(len(i)-1):
        happieness = happieness + findScore(i[j],i[j-1]) + findScore(i[j], i[j+1])
    happieness = happieness + findScore(i[len(i)-1],i[len(i)-2]) + findScore(i[len(i)-1], i[0])
    if happieness>maxHappieness:
        maxHappieness = happieness
print(maxHappieness)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[24] = '2015|Day 13|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()