import time
start = time.process_time()

import re
Input = open('Input.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = re.split(' |,', Input[i])
    if Input[i][0] == 'toggle':
        Input[i][0] = 2
    elif Input[i][1] == 'off':
        Input[i][0] = -1
        Input[i].pop(1)
    elif Input[i][1] == 'on':
        Input[i][0] = 1
        Input[i].pop(1)
    Input[i].pop(3)
lightMatrix = []
for i in range(1000):
    lightMatrix.append([])
    for j in range(1000):
        lightMatrix[i].append(0)
for i in range(len(Input)):
    for j in range(int(Input[i][1]),int(Input[i][3])+1):
        for k in range(int(Input[i][2]),int(Input[i][4])+1):
            #print(j,k)
            if Input[i][0] == 1:
                lightMatrix[j][k] = lightMatrix[j][k]+1
            elif Input[i][0] == -1 and lightMatrix[j][k]>0:
                lightMatrix[j][k] = lightMatrix[j][k]-1
            elif Input[i][0] == 2:
                lightMatrix[j][k] = lightMatrix[j][k]+2
brightness = 0
for i in lightMatrix:
    for j in i:
        brightness = brightness+j
print(brightness)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[11] = '2015|Day 6|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()