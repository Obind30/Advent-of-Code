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
directionInput.append('9')#bro what the actual fuck why did the parser leave out the last 9
inputFile2 = 'AOC-22-2022(1).txt'
mapInput = np.loadtxt(inputFile2, delimiter=' ', dtype='str')
directionBank = [[0,1],[1,0],[0,-1],[-1,0]]
direction = 0
currentPos = [0,50]
#currentPos = [1,9]
for i in range(len(directionInput)):
#for i in range(14):
    print(currentPos, mapInput[currentPos[0]][currentPos[1]])
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
                if nextPos[0]<0 and nextPos[1]>=50 and nextPos[1]<=99:#5a#
                    nextPos = [(nextPos[1]+100),0]
                    direction = 0
                elif nextPos[0]<0 and nextPos[1]>=100 and nextPos[1]<=149:#4a#
                    nextPos = [199, (nextPos[1]-100)]
                    direction = 3
                elif nextPos[1]<50 and nextPos[0]>=0 and nextPos[0]<=49:#6a#
                    nextPos = [(nextPos[0]*-1)+149,0]
                    direction = 0
                elif nextPos[1]>149 and nextPos[0]>=0 and nextPos[0]<=49:#3a#
                    nextPos = [(nextPos[0]*-1)+149,99]
                    direction = 2
                elif nextPos[0]>49 and nextPos[1]>=100 and nextPos[1]<=149:#2a#
                    nextPos = [(nextPos[1]-50),99]
                    direction = 2
                elif nextPos[1]<50 and nextPos[0]>=50 and nextPos[0]<=99:#8a#
                    nextPos = [100, (nextPos[0]-50)]
                    direction = 1
                elif nextPos[1]>99 and nextPos[0]>=50 and nextPos[0]<=99:#2b#
                    nextPos = [49, (nextPos[0]+50)]
                    direction = 3
                elif nextPos[0]<100 and nextPos[1]>=0 and nextPos[1]<=49:#8b#
                    nextPos = [(nextPos[1]+50),50]
                    direction = 0
                elif nextPos[1]<0 and nextPos[0]>=100 and nextPos[0]<=149:#6b#
                    nextPos = [(nextPos[0]*-1)+149, 50]
                    direction = 0
                elif nextPos[1]>99 and nextPos[0]>=100 and nextPos[0]<=149:#3b#
                    nextPos = [(nextPos[0]*-1)+149, 149]
                    directon = 2
                elif nextPos[0]>149 and nextPos[1]>=50 and nextPos[1]<=99:#10a#
                    nextPos = [(nextPos[1]+100),49]
                    direction = 2
                elif nextPos[1]<0 and nextPos[0]>=150 and nextPos[0]<=199:#5b#
                    nextPos = [0, (nextPos[0]-100)]
                    direction = 1
                elif nextPos[1]>49 and nextPos[0]>=150 and nextPos[0]<=199:#10b#
                    nextPos = [149, nextPos[0]-100]
                    direction = 3
                elif nextPos[0]>199 and nextPos[1]>=0 and nextPos[1]<=49:#4b
                    nextPos = [0, nextPos[1]+100]
                    direction = 1
                if mapInput[nextPos[0]][nextPos[1]] == '@':
                    stop = True
                    nextPos = currentPos
                currentPos = nextPos
finalPassword = (1000*((currentPos[0])+1)) + (4*((currentPos[1])+1)) + direction
print(finalPassword)