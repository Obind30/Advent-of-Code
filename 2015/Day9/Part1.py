import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = Input[i].split()
    Input[i].pop(3)
    Input[i].pop(1)
titles = ['AlphaCentauri', 'Snowdin', 'Tambi', 'Faerun', 'Norrath', 'Straylight', 'Tristram','Arbre']
#titles = ['London', 'Dublin', 'Belfast']
distanceMatrix = []
for i in range(len(titles)):
    distanceMatrix.append([])
    for j in range(len(titles)):
        distanceMatrix[i].append(0)
for i in Input:
    distanceMatrix[titles.index(i[0])][titles.index(i[1])] = int(i[2])
    distanceMatrix[titles.index(i[1])][titles.index(i[0])] = int(i[2])
def findPermutations(parentHistory, openList, currentDistance):
    if len(openList) == 1:
        nextDistance = currentDistance + distanceMatrix[titles.index(parentHistory[len(parentHistory)-1])][titles.index(openList[0])]
        return [parentHistory + [openList[0]]+[nextDistance]]
    out = []
    for i in openList:
        if len(parentHistory)>0:
            nextDistance = currentDistance + distanceMatrix[titles.index(parentHistory[len(parentHistory)-1])][titles.index(i)]
        else:
            nextDistance = currentDistance
        if nextDistance>173:
            out.append(parentHistory)
        else:
            appenList = [] #maybe fix this
            for j in openList:
                if not(i == j):
                    appenList.append(j)
            out = out + findPermutations(parentHistory+[i], appenList, nextDistance)
    return out 
permutations = findPermutations([],titles,0)
distances = []
indicies = []
for i in range(len(permutations)):
    if len(permutations[i]) == 9:
        distances.append(permutations[i][8])
        indicies.append(i)
print(min(distances))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[16] = '2015|Day 9|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()