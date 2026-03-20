from array import array
import numpy as np
inputFile = "AOC-24-2022.txt"
input = np.loadtxt(inputFile, delimiter=' ', dtype='str')
gustCoords = []
gustVelocities = []
startPos = [-1,0]
endPos = [4, 5]
#endPos = [25,119]
currentTime = 0
for j in range(len(input)):
    for i in range(len(input[j])):
        if not(input[j][i] == '.'):
            gustCoords.append([int(j), int(i)])
            if input[j][i] == '^':
                gustVelocities.append([-1, 0])
            elif input[j][i] == 'v':
                gustVelocities.append([1, 0])            
            elif input[j][i] == '>':
                gustVelocities.append([0, 1])
            elif input[j][i] == '<':
                gustVelocities.append([0, -1])
def advanceGusts():
    for i in range(len(gustCoords)):
        proposedMove = [gustCoords[i][0]+gustVelocities[i][0], gustCoords[i][1]+gustVelocities[i][1]]
        if proposedMove[0]<0:
            gustCoords[i] = [(len(input)-1), proposedMove[1]]
        elif proposedMove[0]>(len(input)-1):
            gustCoords[i] = [0, proposedMove[1]]
        elif proposedMove[1]<0:
            gustCoords[i] = [proposedMove[0], (len(input[0])-1)]
        elif proposedMove[1]>(len(input[0])-1):
            gustCoords[i] = [proposedMove[0], 0]
        else:
            gustCoords[i] = proposedMove
queue = [startPos]
tempQueue = []
while queue.count(endPos) == 0:
#for k in  range(18):
   visited = []
   advanceGusts()
   for i in range(len(queue)):
       check = [[1,0], [0,1], [-1,0], [0,-1]]
       ass = 0
       for j in range(4):
           attempt = [queue[i][0]+check[j][0], queue[i][1]+check[j][1]]
           if attempt[0]>-1 and attempt[0]<(len(input)+1) and attempt[1]>-1 and attempt[1]<len(input[0]) and gustCoords.count(attempt) == 0 and visited.count(attempt) == 0:
               tempQueue.append(attempt)
               visited.append(attempt)
               ass = ass+1
       if ass == 0 and visited.count(queue[i]) == 0:
           tempQueue.append(queue[i])
           visited.append(queue[i])
   queue = tempQueue
   tempQueue = []
   currentTime = currentTime+1
   print(queue)