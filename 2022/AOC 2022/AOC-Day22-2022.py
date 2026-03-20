from array import array
import numpy as np
inputFile1 = 'AOC-22-2022(2).txt'
with open(inputFile1,'r') as file:
    rawDirectionInput = file.read()
directionInput = []
adding = ''
for i in range(len(rawDirectionInput)):
    if rawDirectionInput[i].isalpha():
        directionInput.append(adding)
        directionInput.append(rawDirectionInput[i])
        adding = '' 
    else:
        adding = adding + rawDirectionInput[i]
directionInput.append('9')#bro what the actual fuck why did the parser leave out the last instruction i litterally hate everything
inputFile2 = 'AOC-22-2022(1).txt'
mapInput = np.loadtxt(inputFile2, delimiter=' ', dtype='str')
directionBank = [[0,1],[1,0],[0,-1],[-1,0]]
direction = 0
currentPos = [1,51]
#currentPos = [1,9]
for i in range(len(directionInput)):
    if directionInput[i] == 'R':
        direction = direction + 1
        if direction>3:
            direction = 0
    elif directionInput[i] == 'L':
        direction = direction - 1
        if direction<0:
            direction = 3
    else:
        stop = False
        for j in range(int(directionInput[i])):
            if not(stop):
                nextPos = [currentPos[0]+directionBank[direction][0],currentPos[1]+directionBank[direction][1]]
                if mapInput[nextPos[0]][nextPos[1]] == '*':
                    loop = True
                    seeker = nextPos
                    while loop:
                        if seeker[0]<0:
                            seeker = [(len(mapInput)-1), seeker[1]]
                        elif seeker[0]>(len(mapInput)-1):
                            seeker = [0, seeker[1]]
                        elif seeker[1]<0:
                            seeker = [seeker[0], len(mapInput[0])-1]
                        elif seeker[1]>(len(mapInput[0])-1):
                            seeker = [seeker[0], 0]
                        if mapInput[seeker[0]][seeker[1]] == '.':
                            loop = False
                            nextPos = seeker
                        elif mapInput[seeker[0]][seeker[1]] == '@':
                            loop = False
                            nextPos = currentPos
                        seeker = [seeker[0]+directionBank[direction][0],seeker[1]+directionBank[direction][1]]
                if mapInput[nextPos[0]][nextPos[1]] == '@':
                    stop = True
                    nextPos = currentPos
                currentPos = nextPos
finalPassword = (1000*(currentPos[0])) + (4*(currentPos[1])) + direction
print(finalPassword)