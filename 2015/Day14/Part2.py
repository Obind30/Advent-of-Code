import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = Input[i].split()
    delList = [1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14]
    for j in reversed(delList):
        Input[i].pop(j)
raceTime = 2503
points = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for k in range(raceTime+1):
    distancesTravelled = []
    for i in range(len(Input)):
        dist = int(Input[i][1])
        timee = int(Input[i][2])+int(Input[i][3])
        repetedDist = dist*int(Input[i][2])*(k//timee)
        if k == 0:
            endDist = 0
        elif k%timee < int(Input[i][2]):
            endDist = dist*(k%timee)
        else:
            endDist = dist*int(Input[i][2])
        distancesTravelled.append(repetedDist+endDist)
    for i in range(len(distancesTravelled)):
        if max(distancesTravelled) > 0 and distancesTravelled[i] == max(distancesTravelled):
            points[i] = points[i] + 1
print(max(points))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[27] = '2015|Day 14|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()