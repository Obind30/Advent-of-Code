import time
start = time.process_time()

Data = open('Input.txt', 'r')
Input = Data.read()
#Input = '^v^v^v^v^v'
currentPos = [0,0]
CurrentRoboPos = [0,0]
visited = [[0,0]]
for i in range(len(Input)):
    if i%2==0:
        if Input[i] == '^':
            currentPos = [currentPos[0], currentPos[1]+1]
        elif Input[i] == '>':
            currentPos = [currentPos[0]+1, currentPos[1]]
        elif Input[i] == 'v':
            currentPos = [currentPos[0], currentPos[1]-1]
        elif Input[i] == '<':
            currentPos = [currentPos[0]-1, currentPos[1]]
        print(currentPos)
        if visited.count(currentPos) == 0:
            visited.append(currentPos)
    else:
        if Input[i] == '^':
            CurrentRoboPos = [CurrentRoboPos[0], CurrentRoboPos[1]+1]
        elif Input[i] == '>':
            CurrentRoboPos = [CurrentRoboPos[0]+1, CurrentRoboPos[1]]
        elif Input[i] == 'v':
            CurrentRoboPos = [CurrentRoboPos[0], CurrentRoboPos[1]-1]
        elif Input[i] == '<':
            CurrentRoboPos = [CurrentRoboPos[0]-1, CurrentRoboPos[1]]
        print(CurrentRoboPos)
        if visited.count(CurrentRoboPos) == 0:
            visited.append(CurrentRoboPos)
print(len(visited))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[5] = '2015|Day 3|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()