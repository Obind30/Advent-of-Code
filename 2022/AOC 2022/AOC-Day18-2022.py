from array import array
import numpy as np
filename = 'AOC-18-2022.txt'
input = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
def arrayContains (Array, thing):
    out = 0
    for i in range(len(Array)):
        arr = Array[i]
        if len(arr) == len(thing):
            if thing[0] == arr[0] and thing[1] == arr[1] and thing[2] == arr[2]:
                return 1
    return 0
surfaceArea = len(input)*6
neighborList = []
def findManhattanDistance(L1, L2, dimensions):
    out = 0
    for i in range(dimensions):
        out = out + abs(L1[i] - L2[i])
    return out
def touchingAir (P1, PointBank):
    adds = [[-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]]
    queue = [P1]
    visited = [P1]
    tempQueue = []
    while arrayContains(queue, [0,0,0]) == 0 and len(queue)>0:
        for j in range(len(queue)):
            for i in range(6):
                checkingPoint = [queue[j][0]+adds[0][i],queue[j][1]+adds[1][i],queue[j][2]+adds[2][i]]
                if not(checkingPoint[0] < -1) and not(checkingPoint[0] > 22) and not(checkingPoint[1] < -1) and not(checkingPoint[1] > 22) and  not(checkingPoint[2] < -1) and not(checkingPoint[2] > 22):
                    if arrayContains(visited, checkingPoint) == 0 and arrayContains(input, checkingPoint) == 0:
                        tempQueue.append(checkingPoint)
                        visited.append(checkingPoint)
        queue = []
        for i in range(len(tempQueue)):
            queue.append(tempQueue[i])
        tempQueue = []
    return arrayContains(queue, [0,0,0])
for i in range(len(input)):
    neighbors = 0
    for j in range(len(input)):
        if findManhattanDistance(input[i],input[j],3) == 1 :
            neighbors = neighbors + 1
    neighborList.append(neighbors)
sum = 0
for j in range(len(input)):
    print(j)
    if not(neighborList[j]) == 6 :
        a = []
        adds = [[-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]]
        for i in range(6):
            a.append([input[j][0]+adds[0][i],input[j][1]+adds[1][i],input[j][2]+adds[2][i]])
        for i in range(6):
            if arrayContains(input, a[i]) == 0 and touchingAir(a[i], input) == 1:
                sum = sum+1
print(sum)