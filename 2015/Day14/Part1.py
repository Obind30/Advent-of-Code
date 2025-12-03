import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = Input[i].split()
    delList = [1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14]
    for j in reversed(delList):
        Input[i].pop(j)
distancesTravelled = []
raceTime = 2503
for i in range(len(Input)):
    dist = int(Input[i][1])
    timee = int(Input[i][2])+int(Input[i][3])
    repetedDist = dist*int(Input[i][2])*(raceTime//timee)
    if raceTime%timee < int(Input[i][2]):
        endDist = dist*(raceTime%timee)
    else:
        endDist = dist*int(Input[i][2])
    distancesTravelled.append(repetedDist+endDist)
print(max(distancesTravelled))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[26] = '2015|Day 14|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()